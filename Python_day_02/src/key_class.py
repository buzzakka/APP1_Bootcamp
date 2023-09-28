class Key:

    def __init__(self) -> None:
        self.passphrase: str = "zax2rulez"

    def __len__(self) -> int:
        return 1337

    def __getitem__(self, key: int):
        return (key + 1) % 6

    def __gt__(self, other: int) -> bool:
        return 9001 > other

    def __str__(self) -> str:
        return "GeneralTsoKeycard"
