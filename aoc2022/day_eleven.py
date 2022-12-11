from dataclasses import dataclass
from typing import List, Callable, Tuple
from operator import add, mul
import math


@dataclass
class Monkey:
    items: List[int]
    opp: Tuple[Callable, int]
    test: Tuple[int, int, int]
    inspections: int = 0


if __name__ == "__main__":
    with open("./inputs/day_eleven.txt") as f:
        lines = f.read().splitlines()

    monkeys = []
    items, opp, test = (None, None, None)
    lines.append("")
    for line in lines:
        if line == "":
            monkeys.append(Monkey(items, opp, test))
            items, opp, test = (None, None, None)
            continue

        split = line.strip().split(":")
        if split[0] == "Starting items":
            items = [int(i) for i in split[1].split(",")]
        elif split[0] == "Operation":
            inst = split[1].split()
            print(inst)
            if inst[-2] == "+":
                opp = (add, int(inst[-1]))
            else:
                if inst[-1] == "old":
                    opp = (mul, -1)
                else:
                    opp = (mul, int(inst[-1]))
        elif split[0] == "Test":
            test = (int(split[1].split()[-1]), 0, 0)
        elif split[0] == "If true":
            test = (test[0], int(split[1].split()[-1]), 0)
        elif split[0] == "If false":
            test = (test[0], test[1], int(split[1].split()[-1]))

    print(monkeys)

    component = 1
    for monkey in monkeys:
        component *= monkey.test[0]

    for i in range(10000):
        for monkey in monkeys:
            while monkey.items:
                monkey.inspections += 1
                item = monkey.items.pop(0)
                factor = item if monkey.opp[1] == -1 else monkey.opp[1]
                item = monkey.opp[0](item, factor)
                item = item % component

                if item % monkey.test[0] == 0:
                    monkeys[monkey.test[1]].items.append(item)
                else:
                    monkeys[monkey.test[2]].items.append(item)

        if i % 1000 == 0:
            print(i)

    print(monkeys)

    inspections = sorted([monkey.inspections for monkey in monkeys], reverse=True)
    print(inspections[0] * inspections[1])
