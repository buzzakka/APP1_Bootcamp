from typing import Dict


def decorator(func):
    def wrapper(*args):
        print("SQUEAK")
        new_purse = func(*args)
        return new_purse
    return wrapper


@decorator
def add_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingot_count: int = get_count_of_ingots(purse)
    new_count: int = ingot_count + 1
    new_purse: Dict[str, int] = {"gold_ingots": new_count}
    return new_purse


@decorator
def get_ingot(purse: Dict[str, int]) -> Dict[str, int]:
    ingot_count: int = get_count_of_ingots(purse)
    new_count: int = (ingot_count, ingot_count - 1)[ingot_count != 0]
    new_purse: Dict[str, int] = {"gold_ingots": new_count}
    return new_purse


@decorator
def empty(purse: Dict[str, int]) -> Dict[str, int]:
    new_purse: Dict[str, int] = {"gold_ingots": 0}
    return new_purse


def get_count_of_ingots(purse: Dict[str, int]) -> int:
    if "gold_ingots" not in purse:
        ingot_count: int = 0
    else:
        ingot_count: int = purse["gold_ingots"]
    return ingot_count