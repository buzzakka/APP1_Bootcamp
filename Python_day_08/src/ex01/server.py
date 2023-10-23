from fastapi import FastAPI, BackgroundTasks
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from uuid import uuid4
from redis import Redis
import aiohttp
import uvicorn


class Args(BaseModel):
    urls: list[str]


class Task(BaseModel):
    status: str = "running"
    id: str


app = FastAPI()
tasks = dict()


async def make_requests(task, urls):
    tasks.update({
        task.id: {
            "task": task,
            "urls": []
        }
    })
    for url in urls:
        tasks[task.id]['urls'].append(await make_request(url))

    task.status = "ready"


async def make_request(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return {"url": url, "status": response.status}


@app.post("/api/v1/tasks/", status_code=201)
async def make_task(args: Args, background_tasks: BackgroundTasks):
    task = Task(id=str(uuid4()))
    background_tasks.add_task(make_requests, task, args.urls)
    return task


@app.get("/api/v1/tasks/{received_task_id}", response_class=HTMLResponse)
async def show_task_info(received_task_id):
    try:
        status = tasks[received_task_id]['task'].status
    except KeyError:
        return "Задача не найдена"
    status = tasks[received_task_id]['task'].status
    if status == "running":
        response = str(tasks[received_task_id]['task'])
    else:
        response = ""
        for url in tasks[received_task_id]["urls"]:
            response += f"<p style='white-space: pre-wrap;'>{url['status']}     {url['url']}</p>"
    return response


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8888, log_level="info")
