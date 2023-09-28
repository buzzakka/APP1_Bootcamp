from typing import Dict


def split_booty(*args: Dict[str, int]):
    ingots_count: int = 0
    for purse in args:
        if "gold_ingots" in purse:
            ingots_count += purse["gold_ingots"]
    purse_1: Dict[str, int] = {"gold_ingots": ingots_count // 3}
    ingots_count -= ingots_count // 3
    purse_2: Dict[str, int] = {"gold_ingots": ingots_count // 2}
    ingots_count -= ingots_count // 2
    purse_3: Dict[str, int] = {"gold_ingots": ingots_count}
    
    return (purse_1, purse_2, purse_3)