from random import randint
from typing import Dict, List


def turrets_generator():
    params = make_params()

    def shoot() -> None:
        print("shoot")

    def search() -> None:
        print("search")

    def talk() -> None:
        print("talk")

    turrent = type("Turret", (object,), {
        "neuroticism": params[0],
        "openness": params[1],
        "conscientiousness": params[2],
        "extraversion": params[3],
        "agreeableness": params[4],
        "shoot": shoot,
        "search": search,
        "talk": talk
    })
    return turrent


def make_params() -> List[int]:
    total = 100
    n = 5

    my_total = -1
    while my_total != total:
        nums = [randint(0, total) for _ in range(n)]
        my_total = sum(nums)

    return nums
