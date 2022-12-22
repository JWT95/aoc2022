DIRECTIONS = [(1, 0), (0, 1), (-1, 0), (0, -1)]
SQUARES = {
    "A": (51, 1),
    "B": (101, 1),
    "C": (51, 51),
    "D": (51, 101),
    "E": (1, 101),
    "F": (1, 151),
}


def part_one(points, instruction):
    position = (min([x for (x, y) in points.keys() if y == 1]), 1)
    direction = 0
    head = 0

    while head < len(instruction):
        # Read the next instruction
        hit_letter = False

        candidate = instruction[head]
        if candidate == "R":
            direction = (direction + 1) % 4
        elif candidate == "L":
            direction = (direction - 1) % 4
        else:
            string = candidate

            while not (
                (head + 1) >= len(instruction) or instruction[head + 1] in ["R", "L"]
            ):
                head += 1
                string += instruction[head]

            move = int(string)

            # Now move
            for i in range(move):
                candidate_position = (
                    position[0] + DIRECTIONS[direction][0],
                    position[1] + DIRECTIONS[direction][1],
                )
                if candidate_position in points:
                    if points[candidate_position] == ".":
                        position = candidate_position
                    else:
                        position = position

                else:
                    # We have wrapped. If the current direction
                    if direction == 0:
                        candidate_position = (
                            min([x for (x, y) in points.keys() if y == position[1]]),
                            position[1],
                        )
                        if points[candidate_position] == ".":
                            position = candidate_position
                        else:
                            position = position
                    if direction == 1:
                        candidate_position = (
                            position[0],
                            min([y for (x, y) in points.keys() if x == position[0]]),
                        )
                        if points[candidate_position] == ".":
                            position = candidate_position
                        else:
                            position = position
                    if direction == 2:
                        candidate_position = (
                            max([x for (x, y) in points.keys() if y == position[1]]),
                            position[1],
                        )
                        if points[candidate_position] == ".":
                            position = candidate_position
                        else:
                            position = position
                    if direction == 3:
                        candidate_position = (
                            position[0],
                            max([y for (x, y) in points.keys() if x == position[0]]),
                        )
                        if points[candidate_position] == ".":
                            position = candidate_position
                        else:
                            position = position

        head += 1

    print(1000 * position[1] + 4 * position[0] + direction)


def part_two(points, instruction):
    position = (min([x for (x, y) in points.keys() if y == 1]), 1)
    print(position)
    direction = 0
    head = 0

    # Parse the points in the square
    # We'll index them by the top left square
    square_map = dict()
    for key, item in SQUARES.items():
        for x in range(50):
            for y in range(50):
                square_map[(item[0] + x, item[1] + y)] = key

    while head < len(instruction):
        # Read the next instruction
        hit_letter = False

        candidate = instruction[head]
        if candidate == "R":
            direction = (direction + 1) % 4
        elif candidate == "L":
            direction = (direction - 1) % 4
        else:
            string = candidate

            while not (
                (head + 1) >= len(instruction) or instruction[head + 1] in ["R", "L"]
            ):
                head += 1
                string += instruction[head]

            move = int(string)

            # Now move
            for i in range(move):
                print(position)
                candidate_position = (
                    position[0] + DIRECTIONS[direction][0],
                    position[1] + DIRECTIONS[direction][1],
                )
                if candidate_position in points:
                    if points[candidate_position] == ".":
                        position = candidate_position
                    else:
                        position = position

                else:
                    print(position, direction, square_map[position])
                    # We have wrapped. See where we are and what direction we are going in
                    if square_map[position] == "A":
                        if direction == 2:
                            candidate_position = (
                                1,
                                SQUARES["E"][1] + 50 - (position[1] - SQUARES["A"][1]),
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 0
                            else:
                                position = position

                        elif direction == 3:
                            candidate_position = (
                                1,
                                SQUARES["F"][1] + position[0] - SQUARES["A"][0],
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 0
                            else:
                                position = position

                    elif square_map[position] == "B":
                        if direction == 3:
                            candidate_position = (
                                SQUARES["F"][0] + position[0] - SQUARES["B"][0],
                                200,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 3
                            else:
                                position = position

                        elif direction == 0:
                            candidate_position = (
                                100,
                                SQUARES["D"][1] + 50 - (position[1] - SQUARES["B"][1]),
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 2
                            else:
                                position = position

                        elif direction == 1:
                            candidate_position = (
                                100,
                                SQUARES["C"][1] + position[0] - SQUARES["B"][0],
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 2
                            else:
                                position = position

                    elif square_map[position] == "C":
                        if direction == 0:
                            candidate_position = (
                                SQUARES["B"][0] + position[1] - SQUARES["C"][1],
                                50,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 3
                            else:
                                position = position

                        elif direction == 2:
                            candidate_position = (
                                SQUARES["E"][0] + position[1] - SQUARES["C"][1],
                                101,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 1
                            else:
                                position = position

                    elif square_map[position] == "D":
                        if direction == 0:
                            candidate_position = (
                                150,
                                SQUARES["B"][1] + 50 - (position[1] - SQUARES["D"][1]),
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 2
                            else:
                                position = position

                        elif direction == 1:
                            candidate_position = (
                                50,
                                SQUARES["F"][1] + position[0] - SQUARES["D"][0],
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 2
                            else:
                                position = position

                    elif square_map[position] == "E":
                        if direction == 2:
                            candidate_position = (
                                51,
                                SQUARES["A"][1] + 50 - (position[1] - SQUARES["E"][1]),
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 0
                            else:
                                position = position

                        elif direction == 3:
                            candidate_position = (
                                51,
                                SQUARES["C"][1] + position[0] - SQUARES["E"][0],
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 0
                            else:
                                position = position

                    elif square_map[position] == "F":
                        if direction == 2:
                            candidate_position = (
                                SQUARES["A"][0] + position[1] - SQUARES["F"][1],
                                1,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 1
                            else:
                                position = position

                        elif direction == 0:
                            candidate_position = (
                                SQUARES["D"][0] + position[1] - SQUARES["F"][1],
                                150,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 3
                            else:
                                position = position

                        elif direction == 1:
                            candidate_position = (
                                SQUARES["B"][0] + position[1] - SQUARES["F"][1],
                                1,
                            )
                            if points[candidate_position] == ".":
                                position = candidate_position
                                direction = 1
                            else:
                                position = position

        head += 1

    print(1000 * position[1] + 4 * position[0] + direction)


if __name__ == "__main__":
    with open("./inputs/day_twentytwo.txt") as f:
        lines = f.read().splitlines()

    points = dict()

    for y in range(201):
        for x in range(len(lines[y])):
            if lines[y][x] == " ":
                pass
            else:
                points[(x + 1, y + 1)] = lines[y][x]

    instruction = lines[201]

    # part_one(points, instruction)
    part_two(points, instruction)
