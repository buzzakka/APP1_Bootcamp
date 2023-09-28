import time
import random


def emit_gel(step: float) -> None:
    press: int = 50
    while True:
        press += random.randint(min(0, step), max(0, step))
        if press > 100:
            press = 100
        time.sleep(0.4)
        print(f"Текущее давление: {press}")
        step = yield press


def valve(step: int = 100) -> None:
    press_gen = emit_gel(step)
    press = next(press_gen)
    while 10 <= press <= 90:
        if press < 20:
            step = abs(step)
        elif press > 80:
            step = -abs(step)
        press = press_gen.send(step)
    else:
        press_gen.close()
        print(f"Достигнуто предельное давление: {press}")


if __name__ == "__main__":
    step = 10
    valve(step)
