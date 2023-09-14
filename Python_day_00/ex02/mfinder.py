import sys
import re


def main() -> None:
    lines = sys.stdin.readlines()
    error_flag: bool = (
        len(lines) != 3 or len(lines[0].strip('\n')) != 5 or
        len(lines[1].strip('\n')) != 5 or len(lines[2]) != 5
        or lines[2].endswith('\n')
    )
    if not error_flag:
        result_status = (
            re.fullmatch(r'^\*[^*]{3}\*\n$', lines[0]) is not None
            and re.fullmatch(r'^\*\*[^*]\*\*\n$', lines[1]) is not None
            and re.fullmatch(r'^\*[^*]\*[^*]\*$', lines[2]) is not None
        )
        print(result_status)
    else:
        print('Ошибка')


if __name__ == "__main__":
    try:
        main()
    except:
        print("Возникла ошибка при выполнении программы")
