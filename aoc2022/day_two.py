from __future__ import annotations
from enum import Enum


class RPS(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3

    @classmethod
    def from_text(cls, c: str) -> RPS:
        if c in ["A", "X"]:
            return RPS.ROCK
        elif c in ["B", "Y"]:
            return RPS.PAPER
        elif c in ["C", "Z"]:
            return RPS.SCISSORS
        else:
            raise Exception("Unknown char %s", c)

    def will_lose_to(self) -> RPS:
        return RPS((self.value % 3) + 1)

    def will_beat(self) -> RPS:
        return RPS((self.value + 1) % 3 + 1)

    def beats(self, other: RPS) -> int:
        if self == other:
            return 0
        elif other == self.will_lose_to():
            return -1
        else:
            return 1

    def score(self, other):
        return (self.beats(other) + 1) * 3 + self.value

    @classmethod
    def optimal_move(cls, other: RPS, strategy: str) -> RPS:
        if strategy == "X":
            return other.will_beat()
        elif strategy == "Y":
            return other
        else:
            return other.will_lose_to()


if __name__ == "__main__":
    with open("./inputs/day_two.txt") as f:
        turns = [line.split() for line in f.read().splitlines()]

    print(sum([RPS.from_text(turn[1]).score(RPS.from_text(turn[0])) for turn in turns]))

    print(
        sum(
            [
                RPS.optimal_move(RPS.from_text(turn[0]), turn[1]).score(
                    RPS.from_text(turn[0])
                )
                for turn in turns
            ]
        )
    )
