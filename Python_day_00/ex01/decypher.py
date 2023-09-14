import argparse


def main() -> None:
    parser = argparse.ArgumentParser(description="Decryption of the message")
    parser.add_argument("message", type=str,
                        help="The message that needs to be decrypted")

    args = parser.parse_args()

    for index in range(len(args.message.strip())):
        if index == 0 or args.message[index - 1] == ' ':
            print(args.message[index], end='')


if __name__ == "__main__":
    try:
        main()
    except:
        print("Возникла ошибка при выполнении программы")
