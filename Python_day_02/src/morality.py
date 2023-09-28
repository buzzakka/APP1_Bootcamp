from collections import Counter
from itertools import combinations


class Player:

    def __init__(self) -> None:
        self.move: str = None

    def cheat(self) -> None:
        self.move = "cheat"

    def cooperate(self) -> None:
        self.move = "cooperate"

    def reset(self) -> None:
        self.move = None


class Cheater(Player):

    def make_move(self) -> None:
        self.cheat()

    def __str__(self) -> str:
        return "Cheater"


class Cooperator(Player):

    def make_move(self) -> None:
        self.cooperate()

    def __str__(self) -> str:
        return "Cooperator"


class Copycat(Player):

    def make_move(self, others_move: str) -> None:
        if not others_move or others_move == "cooperate":
            self.cooperate()
        else:
            self.cheat()

    def __str__(self) -> str:
        return "Copycat"


class Grudger(Player):

    def make_move(self, others_move: str) -> None:
        if others_move == "cheat" or self.move == "cheat":
            self.cheat()
        else:
            self.cooperate()

    def __str__(self) -> str:
        return "Grudger"


class Detective(Copycat, Cheater):

    def __init__(self):
        super().__init__()
        self.was_cheated: bool = False

    def make_move(self, others_move: str, round: int) -> None:
        moves = [self.cooperate, self.cheat, self.cooperate, self.cooperate]
        if others_move == "cheat":
            self.was_cheated = True
        if round <= 3:
            moves[round]()
        elif self.was_cheated:
            Copycat.make_move(self, others_move)
        else:
            Cheater.make_move(self)

    def reset(self) -> None:
        super().reset()
        self.was_cheated = False

    def __str__(self) -> str:
        return "Detective"


# Поступает как Copycat, но в последнем раунде обманывает
class CustomPlayer(Copycat):

    def make_move(self, others_move: str, is_last_round: bool) -> None:
        if not is_last_round:
            super().make_move(others_move)
        else:
            self.cheat()

    def __str__(self) -> str:
        return "CustomPlayer"


class Game:

    def __init__(self, matches=10):
        self.matches = matches
        self.registry = Counter()

    def play(self, player1, player2):
        for round in range(self.matches):
            p1_prev_move = player1.move
            p2_prev_move = player2.move
            self.make_move(player1, p2_prev_move, round)
            self.make_move(player2, p1_prev_move, round)
            self.count_candyes(player1, player2)
        player1.reset()
        player2.reset()

    def make_move(self, player, other_players_move: str, round: int):
        if str(player) in ("Cheater", "Cooperator"):
            player.make_move()
        elif str(player) in ("Copycat", "Grudger"):
            player.make_move(other_players_move)
        elif str(player) == "Detective":
            player.make_move(other_players_move, round)
        else:
            player.make_move(other_players_move, round == self.matches - 1)

    def count_candyes(self, p1, p2):
        p1_move = p1.move
        p2_move = p2.move

        if p1_move == "cooperate" and p2_move == "cooperate":
            self.registry[str(p1)] += 2
            self.registry[str(p2)] += 2
        elif p1_move == "cheat" and p2_move == "cooperate":
            self.registry[str(p1)] += 3
            self.registry[str(p2)] -= 1
        elif p1_move == "cooperate" and p2_move == "cheat":
            self.registry[str(p1)] -= 1
            self.registry[str(p2)] += 3

    def top3(self):
        for elem in self.registry.most_common(3):
            player, score = elem
            print(player, score)


if __name__ == "__main__":
    game = Game()
    players = [Copycat(), Cheater(), Cooperator(), Grudger(),
               Detective()]
    combination = combinations(players, 2)
    for p1, p2 in combination:
        game.play(p1, p2)
    game.top3()
