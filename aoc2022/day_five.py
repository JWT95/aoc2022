if __name__ == "__main__":
    with open("./inputs/day_five.txt") as f:
        lines = f.read().splitlines()

    diagram = []
    instructions = []
    found_blank_line = False

    for line in lines:
        if not line:
            found_blank_line = True
            continue

        if not found_blank_line:
            diagram.append(line)
        else:
            instructions.append(line)

    # Process instructions
    diagram_parsed = [[] for _ in range(9)]

    # Get rid of the bottom line of the diagram
    diagram = diagram[:-1]

    for line in reversed(diagram):
        for i in range(9):
            index = 4 * i + 1
            if index < len(line) and line[index] and line[index] != " ":
                diagram_parsed[i].append(line[index])

    # Now go through and parse the instructions
    instructions_parsed = [
        (int(line.split()[1]), int(line.split()[3]), int(line.split()[5]))
        for line in instructions
    ]

    print(diagram_parsed)
    print(instructions_parsed)

    # Now play through the instructions - Part One
    # for instruction in instructions_parsed:
    #     for _ in range(instruction[0]):
    #         diagram_parsed[instruction[2] - 1].append(
    #             diagram_parsed[instruction[1] - 1].pop()
    #         )

    # Part Two
    for instruction in instructions_parsed:
        diagram_parsed[instruction[2] - 1].extend(
            diagram_parsed[instruction[1] - 1][-instruction[0] :]
        )
        diagram_parsed[instruction[1] - 1] = diagram_parsed[instruction[1] - 1][
            0 : -instruction[0]
        ]

    string = ""
    for d in diagram_parsed:
        if d:
            string += d[-1]

    print(string)
