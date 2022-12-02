if __name__ == "__main__":
    with open("./inputs/day_one.txt") as f:
        lines = f.read().splitlines()

    # Build up a list of food by elf
    elves = []
    current_count = 0
    for line in lines:
        if line:
            current_count += int(line)
        else:
            elves.append(current_count)
            current_count = 0

    print(max(elves))
    print(sum(sorted(elves, reverse=True)[0:3]))
