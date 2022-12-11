from typing import List, Tuple


def tree_is_visible_line(trees: List[int], position: int) -> bool:
    if position == 0:
        return True
    else:
        return max(trees[:position]) < trees[position]


def tree_score_direction(trees: List[int], position: int) -> int:
    # We only care about the slice
    if position == 0:
        return 0

    slice_of_interest = list(reversed(trees[:position]))
    for i in range(len(slice_of_interest)):
        if slice_of_interest[i] >= trees[position]:
            break

    return i + 1


def tree_is_visible_square(trees: List[List[int]], x: int, y: int) -> bool:
    # Find if visible from west
    if tree_is_visible_line(trees[y], x):
        return True
    if tree_is_visible_line(list(reversed(trees[y])), len(trees[0]) - x - 1):
        return True
    if tree_is_visible_line([line[x] for line in trees], y):
        return True
    if tree_is_visible_line(
        list(reversed([line[x] for line in trees])),
        len(trees) - 1 - y,
    ):
        return True
    return False


def tree_score(trees: List[List[int]], x: int, y: int) -> int:
    score = 1
    score *= tree_score_direction(trees[y], x)
    score *= tree_score_direction(list(reversed(trees[y])), len(trees[0]) - x - 1)
    score *= tree_score_direction([line[x] for line in trees], y)
    score *= tree_score_direction(
        list(reversed([line[x] for line in trees])), len(trees) - 1 - y
    )
    return score


if __name__ == "__main__":
    with open("./inputs/day_eight.txt") as f:
        lines = f.read().splitlines()

    values = [[int(i) for i in line] for line in lines]

    sum = 0
    for y in range(len(values)):
        for x in range(len(values[0])):
            if tree_is_visible_square(values, x, y):
                sum += 1

    print(sum)

    max_score = 0
    for y in range(len(values)):
        for x in range(len(values[0])):
            score = tree_score(values, x, y)
            if score > max_score:
                max_score = score

    print(max_score)
