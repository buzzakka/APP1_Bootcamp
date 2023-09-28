import redis
from typing import Dict, List
import logging
import json
from random import choice, randint
from time import sleep


numbers: List[int] = [
    2222222222,
    5555555555,
    1111111111,
    1234567890,
    12345,
    4444444444,
    00000000000
]


def main() -> None:
    with redis.Redis() as redis_client:
        while True:
            value = 33333 * randint(-1, 5)
            add_new_transaction(redis_client, choice(numbers), choice(numbers), value)
            sleep(1)


def add_new_transaction(redis_client: redis, from_num: int, to_num: int, amount: int) -> None:
    if is_correct_numbers(from_num, to_num):
        json_data = make_json(from_num, to_num, amount)
        redis_client.lpush("queue", json.dumps(json_data))
        logger(json_data)


def is_correct_numbers(from_num: int, to_num: int) -> bool:
    if len(str(from_num)) == 10 and len(str(to_num)) == 10:
        return True
    else:
        logger(None)
        return False


def make_json(from_num: int, to_num: int, amount: int) -> dict:
    json_data = {
        "metadata": {
            "from": from_num,
            "to": to_num
        },
        "amount": amount
    }
    return json_data


def logger(data: dict):
    logging.basicConfig(level=logging.DEBUG)
    if data:
        logging.info(f"The entry was made successfully: {data}")
    else:
        logging.error(
            "Incorrect input data: the length of account numbers should be equal to 10.")


if __name__ == "__main__":
    main()
