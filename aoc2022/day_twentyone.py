from operator import add, mul, sub, floordiv

def part_one(monkeys):
    found_root = False
    while not found_root:
        for monkey, value in monkeys.items():
            if not isinstance(value, int):
                if isinstance(monkeys[value[0]], int) and isinstance(monkeys[value[2]], int) :
                    monkeys[monkey] = value[1](monkeys[value[0]], monkeys[value[2]])

                    if monkey == "root":
                        print(monkeys["root"])
                        found_root = True

def part_two(monkeys):
    # Go for 5000 cycles
    monkeys["humn"] = ("humn", add, "humn")
    for i in range(10000):
        for monkey, value in monkeys.items():
            if not isinstance(value, int):
                if not isinstance(value[0], int) and isinstance(monkeys[value[0]], int):
                    monkeys[monkey] = (monkeys[value[0]], value[1], value[2])

                if not isinstance(value[2], int) and isinstance(monkeys[value[2]], int):
                    monkeys[monkey] = (monkeys[monkey][0], value[1], monkeys[value[2]])

                if isinstance(value[0], int)   and isinstance(value[2], int):
                    monkeys[monkey] = value[1](value[0], value[2])

                    if monkey == "root":
                        found_root = True

    # Now reverse the equation
    monkeys["humn"] = ("humn", add, "humn")
    new_monkeys = dict()
    for monkey, value in monkeys.items():
        if not isinstance(value, int) and not monkey == "humn":
            # Find the entry which is unresolved
            if not isinstance(value[0], int):
                if value[1] == add:
                    new_op = sub
                if value[1] == sub:
                    new_op = add
                if value[1] == mul:
                    new_op = floordiv
                if value[1] == floordiv:
                    new_op = mul

                new_monkeys[value[0]] = (monkey, new_op, value[2])

            if not isinstance(value[2], int):
                if value[1] == add:
                    new_op = sub
                    new_monkeys[value[2]] = (monkey, new_op, value[0])
                if value[1] == sub:
                    new_op = sub
                    new_monkeys[value[2]] = (value[0], new_op, monkey)
                if value[1] == mul:
                    new_op = floordiv
                    new_monkeys[value[2]] = (monkey, new_op, value[0])
                if value[1] == floordiv:
                    new_op = floordiv
                    new_monkeys[value[2]] = (value[0], new_op, monkey)


    new_monkeys[monkeys["root"][0]] = monkeys["root"][2]
    found_root = False
    while not found_root:
        for monkey, value in new_monkeys.items():
            if not isinstance(value, int):
                if not isinstance(value[0], int) and isinstance(new_monkeys[value[0]], int):
                    new_monkeys[monkey] = (new_monkeys[value[0]], value[1], value[2])

                if not isinstance(value[2], int) and isinstance(new_monkeys[value[2]], int):
                    new_monkeys[monkey] = (new_monkeys[monkey][0], value[1], new_monkeys[value[2]])

                if isinstance(value[0], int)   and isinstance(value[2], int):
                    new_monkeys[monkey] = value[1](value[0], value[2])

                    if monkey == "humn":
                        found_root = True
                        print(new_monkeys["humn"])


if __name__ == "__main__":
    with open("./inputs/day_twentyone.txt") as f:
        lines = f.read().splitlines()

    # Monkeys
    monkeys = dict()

    for line in lines:
        line = line.split()
        monkey = line[0].strip(":")

        if len(line) == 2:
            monkeys[monkey] = int(line[1])

        else:
            if line[2] == "*":
                monkeys[monkey] = (line[1], mul, line[3])
            if line[2] == "+":
                monkeys[monkey] = (line[1], add, line[3])
            if line[2] == "-":
                monkeys[monkey] = (line[1], sub, line[3])
            if line[2] == "/":
                monkeys[monkey] = (line[1], floordiv, line[3])

    monkeys_one = {monkey: value for monkey, value in monkeys.items()}
    part_one(monkeys_one)
    part_two(monkeys)
