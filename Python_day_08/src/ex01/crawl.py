import argparse
import logging
from urllib.parse import urlparse
import aiohttp
import asyncio

logging.basicConfig(level=logging.WARNING, format="%(asctime)s %(levelname)s %(message)s")

POST_URL = 'http://127.0.0.1:8888/api/v1/tasks/'


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('URLs', type=str, nargs='+')
    return parser.parse_args().URLs


async def main():
    args = get_args()
    data = {"urls": []}
    for arg in args:
        if urlparse(arg).netloc == '':
            logging.warning(f'{arg} - некорректная ссылка')
        else:
            data['urls'].append(arg)
    async with aiohttp.ClientSession() as session:
        response = await session.post(POST_URL, json=data)
        if response.status == 201:
            print(await response.json())
        


if __name__ == "__main__":
    asyncio.run(main())
