from dijkstar import Graph
from typing import List, Set, Tuple


def part_one(
    points, blizzards, start_point, end_point
) -> Tuple[Set[Tuple[int, int]], int]:
    elf_points = {start_point}
    for i in range(10000):
        # Move the blizzards
        new_blizzards = set()
        for blizzard in blizzards:
            if blizzard[1] == ">":
                new_point = (blizzard[0][0] + 1, blizzard[0][1])
                if new_point in points:
                    new_blizzards.add((new_point, blizzard[1]))
                else:
                    new_blizzards.add(((1, blizzard[0][1]), blizzard[1]))

            if blizzard[1] == "<":
                new_point = (blizzard[0][0] - 1, blizzard[0][1])
                if new_point in points:
                    new_blizzards.add((new_point, blizzard[1]))
                else:
                    new_blizzards.add(
                        ((len(lines[0]) - 2, blizzard[0][1]), blizzard[1])
                    )

            if blizzard[1] == "^":
                new_point = (blizzard[0][0], blizzard[0][1] - 1)
                if new_point in points:
                    new_blizzards.add((new_point, blizzard[1]))
                else:
                    new_blizzards.add(((blizzard[0][0], len(lines) - 2), blizzard[1]))

            if blizzard[1] == "v":
                new_point = (blizzard[0][0], blizzard[0][1] + 1)
                if new_point in points:
                    new_blizzards.add((new_point, blizzard[1]))
                else:
                    new_blizzards.add(((blizzard[0][0], 1), blizzard[1]))

        blizzards = new_blizzards

        # Now move the elf
        new_elf_points = set()
        blizzard_set = {blizzard[0] for blizzard in blizzards}
        for point in elf_points:
            for delta in [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]:
                new_point = (point[0] + delta[0], point[1] + delta[1])
                if new_point in points and new_point not in blizzard_set:
                    new_elf_points.add(new_point)

        elf_points = new_elf_points

        if end_point in elf_points:
            return (blizzards, i + 1)


def part_two(points, blizzards, start_point, end_point):
    blizzards, out = part_one(points, blizzards, start_point, end_point)
    blizzards, back = part_one(points, blizzards, end_point, start_point)
    blizzards, out_again = part_one(points, blizzards, start_point, end_point)

    return out + back + out_again


if __name__ == "__main__":
    with open("./inputs/day_twentyfour.txt") as f:
        lines = f.read().splitlines()

    points = set()
    blizzards = set()
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if not lines[y][x] == "#":
                points.add((x, y))
                if not lines[y][x] == ".":
                    blizzards.add(((x, y), lines[y][x]))

    start_point = [point for point in points if point[1] == 0][0]
    end_point = [point for point in points if point[1] == len(lines) - 1][0]

    print(part_one(points, blizzards, start_point, end_point)[1])
    print(part_two(points, blizzards, start_point, end_point))
