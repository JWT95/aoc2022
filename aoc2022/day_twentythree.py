from typing import Tuple
from dataclasses import dataclass

INSTRUCTIONS = ["N", "S", "W", "E"]
MOVES = [(-1, -1), (0, -1), (1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0)]


@dataclass
class Elf:
    original_position: Tuple[int, int]
    current_position: Tuple[int, int]

    def propose_move(self, grid, current_direction) -> Tuple[int, int]:
        found_match = False
        for delta in MOVES:
            if (
                self.current_position[0] + delta[0],
                self.current_position[1] + delta[1],
            ) in grid:
                found_match = True
                break

        if not found_match:
            return self.current_position

        for i in range(4):
            direction = INSTRUCTIONS[(current_direction + i) % 4]
            if direction == "N":
                blocked = False
                for delta in [MOVES[0], MOVES[1], MOVES[2]]:
                    if (
                        self.current_position[0] + delta[0],
                        self.current_position[1] + delta[1],
                    ) in grid:
                        blocked = True
                        break
                if not blocked:
                    return (self.current_position[0], self.current_position[1] - 1)
            if direction == "S":
                blocked = False
                for delta in [MOVES[4], MOVES[5], MOVES[6]]:
                    if (
                        self.current_position[0] + delta[0],
                        self.current_position[1] + delta[1],
                    ) in grid:
                        blocked = True
                        break
                if not blocked:
                    return (self.current_position[0], self.current_position[1] + 1)
            if direction == "W":
                blocked = False
                for delta in [MOVES[0], MOVES[3], MOVES[4]]:
                    if (
                        self.current_position[0] + delta[0],
                        self.current_position[1] + delta[1],
                    ) in grid:
                        blocked = True
                        break
                if not blocked:
                    return (self.current_position[0] - 1, self.current_position[1])
            if direction == "E":
                blocked = False
                for delta in [MOVES[2], MOVES[6], MOVES[7]]:
                    if (
                        self.current_position[0] + delta[0],
                        self.current_position[1] + delta[1],
                    ) in grid:
                        blocked = True
                        break
                if not blocked:
                    return (self.current_position[0] + 1, self.current_position[1])

        return self.current_position


if __name__ == "__main__":
    with open("./inputs/day_twentythree.txt") as f:
        lines = f.read().splitlines()

    elves = dict()

    for y in range(len(lines)):
        for x in range(len(lines[0])):
            if lines[y][x] == "#":
                elves[(x, y)] = Elf((x, y), (x, y))

    for i in range(100000):
        # Propose a move for each elf
        proposed_positions = dict()
        for point, elf in elves.items():
            proposed_position = elf.propose_move(elves, i)

            if proposed_position in proposed_positions:
                proposed_positions[proposed_position].append(elf)
            else:
                proposed_positions[proposed_position] = [elf]

        # Now make a new grid
        new_elves = dict()
        for position, item in proposed_positions.items():
            if len(item) == 1:
                elf = proposed_positions[position][0]
                elf.current_position = position
                new_elves[position] = elf
            else:
                for elf in item:
                    new_elves[elf.current_position] = elf

        if elves == new_elves:
            print(i + 1)
            break
        else:
            elves = new_elves

    # Find the largest rectangle
    min_x = min(x for x, y in elves)
    min_y = min(y for x, y in elves)
    max_x = max(x for x, y in elves)
    max_y = max(y for x, y in elves)

    count = 0
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            if not (x, y) in elves:
                count += 1

    print(count)
