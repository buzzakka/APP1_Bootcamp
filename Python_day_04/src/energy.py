from itertools import zip_longest
from typing import List


def fix_wiring(cables: List[str], sockets: List[str], plugs: List[str]) -> List[str]:
    f_plugs: List[str] = [
        plug for plug in plugs if str(plug).startswith("plug")]
    f_sockets: List[str] = [
        socket for socket in sockets if str(socket).startswith("socket")]
    f_cables: List[str] = [
        cable for cable in cables if str(cable).startswith("cable")]
    combo: List[str] = list(zip_longest(
        [list(li) for li in zip(f_cables, f_sockets)], f_plugs, fillvalue=None))

    result = [
        f"plug {elem[0][0]} into {elem[0][1]} using {elem[1]}" if elem[1]
        else f"weld {elem[0][0]} to {elem[0][1]} without plug"
        for elem in combo
        if elem[0]
    ]

    return result
