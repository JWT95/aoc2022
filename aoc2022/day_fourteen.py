def part_one(grid):
    count = 0
    while True:
        position = (500, 0)
        settled = False
        for i in range(1000):
            attempted_moves = [(0, 1), (-1, 1), (1, 1)]
            moved = False
            for attempted_move in attempted_moves:
                if (
                    not (
                        position[0] + attempted_move[0],
                        position[1] + attempted_move[1],
                    )
                    in grid
                ):
                    position = (
                        position[0] + attempted_move[0],
                        position[1] + attempted_move[1],
                    )
                    moved = True
                    break

            if not moved:
                grid.add(position)
                settled = True
                break

        if not settled:
            break
        else:
            count += 1

    print(count)


def part_two(grid):
    # First find the highest y
    max_y = max([point[1] for point in grid])

    # Then add the line to the grid
    for i in range(-1000, 1000):
        grid.add((i, max_y + 2))

    # Now do the same calculation again
    count = 0
    while True:
        position = (500, 0)
        settled = False
        for i in range(1000):
            attempted_moves = [(0, 1), (-1, 1), (1, 1)]
            moved = False
            for attempted_move in attempted_moves:
                if (
                    not (
                        position[0] + attempted_move[0],
                        position[1] + attempted_move[1],
                    )
                    in grid
                ):
                    position = (
                        position[0] + attempted_move[0],
                        position[1] + attempted_move[1],
                    )
                    moved = True
                    break

            if not moved:
                grid.add(position)
                settled = True
                break

        if not settled:
            break
        else:
            count += 1
            if position == (500, 0):
                break

    print(count)


if __name__ == "__main__":
    with open("./inputs/day_fourteen.txt") as f:
        lines = f.read().splitlines()

    grid = set()
    for line in lines:
        splitline = line.split(" -> ")
        for i in range(len(splitline) - 1):
            old = [int(j) for j in splitline[i].split(",")]
            new = [int(j) for j in splitline[i + 1].split(",")]

            if old[0] < new[0]:
                for i in range(old[0], new[0] + 1):
                    grid.add((i, new[1]))
            elif old[0] > new[0]:
                for i in range(new[0], old[0] + 1):
                    grid.add((i, new[1]))
            if old[1] < new[1]:
                for i in range(old[1], new[1] + 1):
                    grid.add((old[0], i))
            elif old[1] > new[1]:
                for i in range(new[1], old[1] + 1):
                    grid.add((old[0], i))

    part_one({point for point in grid})
    part_two(grid)
