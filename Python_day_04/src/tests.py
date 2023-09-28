from personality import turrets_generator
from energy import fix_wiring


# Вспомогательная функция для вывода всех параметров класса
def turrent_print(turrent=turrets_generator()) -> None:
    print("turrent_structure:")
    print(f"neuroticism:\t\t{turrent.neuroticism}")
    print(f"openness:\t\t{turrent.openness}")
    print(f"conscientiousness:\t{turrent.conscientiousness}")
    print(f"extraversion:\t\t{turrent.extraversion}")
    print(f"agreeableness:\t\t{turrent.agreeableness}")
    turrent.shoot()
    turrent.search()
    turrent.talk()


def energy_test_1() -> bool:
    plugs = ['plug1', 'plug2', 'plug3']
    sockets = ['socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable1', 'cable2', 'cable3', 'cable4']

    print("""Energy_test_1:
Right output:
plug cable1 into socket1 using plug1
plug cable2 into socket2 using plug2
plug cable3 into socket3 using plug3
weld cable4 to socket4 without plug

Program output:""")

    for c in fix_wiring(cables, sockets, plugs):
        print(c)


def energy_test_2() -> bool:
    plugs = ['plugZ', None, 'plugY', 'plugX']
    sockets = [1, 'socket1', 'socket2', 'socket3', 'socket4']
    cables = ['cable2', 'cable1', False]

    print("""
Energy_test_2:
Right output:
plug cable2 into socket1 using plugZ
plug cable1 into socket2 using plugY

Program output:""")

    for c in fix_wiring(cables, sockets, plugs):
        print(c)


# В тесте закоменченная строка позволит выводить параметры сгенерированных турелей
def turrent_test_1(count: int = 5) -> bool:
    for _ in range(count):
        turrent = turrets_generator()
        # turrent_print(turrent)
        result = turrent.neuroticism + turrent.openness + \
            turrent.conscientiousness + turrent.extraversion + turrent.agreeableness
        if not result:
            return False
    return True


if __name__ == "__main__":
    energy_test_1()
    energy_test_2()
    print(f"\nTurrent_test_1: {turrent_test_1()}")
