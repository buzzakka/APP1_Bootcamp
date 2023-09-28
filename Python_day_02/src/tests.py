import key_class
from morality import *


def test_ex00() -> bool:
    key = key_class.Key()
    result = (
        len(key) == 1337 and
        key[404] == 3 and
        key > 9000 and
        key.passphrase == "zax2rulez" and
        str(key) == "GeneralTsoKeycard"
    )
    return result


def test_ex01() -> bool:
    game = Game(1)
    players = [Copycat(), Cheater(), Cooperator(), Grudger(),
               Detective(), CustomPlayer()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    result_flag = (
        game.registry["Cheater"] == 12 and
        game.registry["CustomPlayer"] == 12 and
        game.registry["Copycat"] == 4 and
        game.registry["Cooperator"] == 4 and
        game.registry["Grudger"] == 4 and
        game.registry["Detective"] == 4
    )
    return result_flag


def test_ex02() -> bool:
    game = Game(10)
    players = [Copycat(), Cheater(), Cooperator(), Grudger(),
               Detective(), CustomPlayer()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    result_flag = (
        game.registry["CustomPlayer"] == 81 and
        game.registry["Copycat"] == 74 and
        game.registry["Grudger"] == 63 and
        game.registry["Detective"] == 60 and
        game.registry["Cheater"] == 48 and
        game.registry["Cooperator"] == 46
    )
    return result_flag


if __name__ == "__main__":
    print(f"Test_01: {test_ex00()}")
    print(f"Test_02: {test_ex01()}")
    print(f"Test_02: {test_ex02()}")
