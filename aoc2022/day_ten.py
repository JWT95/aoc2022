if __name__ == "__main__":
    with open("./inputs/day_ten.txt") as f:
        lines = f.read().splitlines()

    register = 1
    cycles = [1]

    for line in lines:

        if line == "noop":
            cycles.append(register)
            continue

        add = line.split()
        cycles.append(register)
        register += int(add[1])
        cycles.append(register)

    a = [cycles[i] * (i + 1) for i in [19, 59, 99, 139, 179, 219]]
    print(sum(a))

    screen_str = ""
    for i in range(len(cycles)):
        if i % 40 == 0:
            print(screen_str)
            screen_str = ""

        if cycles[i] - 1 <= i % 40 <= cycles[i] + 1:
            screen_str += "."
        else:
            screen_str += "#"
