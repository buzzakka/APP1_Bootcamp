import argparse
import redis
import json
from typing import List
import logging


def main() -> None:
    with redis.Redis() as redis_client:
        hack_numbers(redis_client)


def hack_numbers(redis_client: redis):
    evil_numbers = parser()
    while(True):
        while (redis_client.llen("queue") != 0):
            temp = redis_client.rpop("queue").decode()
            data = json.loads(temp)
            logger(data)
            if data["metadata"]["to"] in evil_numbers and data["amount"] >= 0:
                data["metadata"] = {
                    "from": data["metadata"]["to"],
                    "to": data["metadata"]["from"]
                }
                logger(data, "hacked")


def logger(data: dict, status: str = "normal"):
    logging.basicConfig(level=logging.DEBUG)
    if status == "hacked":
        logging.info(f"The data was successfully hacked: {data}")
    else:
        logging.info(f"New input data: {data}")


def parser() -> List[int]:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-e', help="List of bad guys account numbers", required=True)
    args = parser.parse_args()
    numbers = [int(num) for num in args.e.split(',')]
    return numbers


if __name__ == "__main__":
    main()
