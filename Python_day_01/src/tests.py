#!/usr/bin/python3
import ingot
import split_booty
from typing import Dict


def compare_dicts(d1: Dict[str, int], d2: Dict[str, int]) -> bool:
    result: bool = len(d1) == len(d2) and d1 == d2
    return result


def ingot_test() -> None:
    print("Ingot and SQUEAK test:")
    purse: Dict[str, int] = {}
    next_purse: Dict[str, int] = ingot.empty(purse)
    test_flag = compare_dicts(next_purse, {"gold_ingots": 0}) and purse is not next_purse
    
    purse = next_purse
    next_purse = ingot.get_ingot(next_purse)
    test_flag = test_flag and compare_dicts(next_purse, {"gold_ingots": 0}) and next_purse is not purse
    
    purse = next_purse
    next_purse = ingot.add_ingot(purse)
    test_flag = test_flag and compare_dicts(next_purse, {"gold_ingots": 1}) and next_purse is not purse
    
    purse = next_purse
    next_purse = ingot.add_ingot(ingot.get_ingot(ingot.add_ingot(ingot.empty(purse))))
    test_flag = test_flag and compare_dicts(next_purse, {"gold_ingots": 1}) and next_purse is not purse
    
    purse = next_purse
    next_purse = ingot.add_ingot(ingot.add_ingot(ingot.add_ingot(next_purse)))
    test_flag = test_flag and compare_dicts(next_purse, {"gold_ingots": 4}) and next_purse is not purse
    
    purse = next_purse
    next_purse = ingot.get_ingot(ingot.get_ingot(ingot.get_ingot(ingot.empty(purse))))
    test_flag = test_flag and compare_dicts(next_purse, {"gold_ingots": 0}) and next_purse is not purse
    
    print(test_flag)


def split_booty_test() -> None:
    print("Split booty test:")
    for i in range(20):
        purse_1 = {"gold_ingots": i}
        purse_2 = {"gold": i}
        purse_3 = {"ingots": i}
        
        res = split_booty.split_booty(purse_1, purse_2, purse_3)
        res_purse_1 = res[0]
        res_purse_2 = res[1]
        res_purse_3 = res[2]
        temp_i = i
        i_1 = i // 3
        i -= i_1
        i_2 = i // 2
        i_3 = i - i_2
        test_flag = sorted([i_1, i_2, i_3]) == sorted([res_purse_1["gold_ingots"], res_purse_2["gold_ingots"], res_purse_3["gold_ingots"]])
        if not test_flag:
            break
    print(test_flag)


if __name__ == "__main__":
    ingot_test()
    split_booty_test()