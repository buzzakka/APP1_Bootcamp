import argparse
import sys


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Finds lines with only 5 zeros in begin and length = 32 symbols")
    parser.add_argument("num", type=int, help="Number of lines for the parser")

    args = parser.parse_args()

    for _ in range(args.num):
        line: str = sys.stdin.readline().strip()
        if len(line) == 32 and line.startswith("00000") and line[5] != "0":
            print(line)


if __name__ == "__main__":
    try:
        main()
    except:
        print("Возникла ошибка при выполнении программы")
