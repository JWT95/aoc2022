from typing import List


def char_score(char: str):
    if char.isupper():
        return ord(char) - 38
    else:
        return ord(char) - 96


def common_char(strings: List[str]):
    common_chars = strings[0]
    for string in strings[1:]:
        for char in common_chars:
            if char not in string:
                common_chars = common_chars.replace(char, "")

    return common_chars[0]


def part_one(lines: List[str]):
    common_chars = [common_char([left, right]) for left, right in parsed_lines]
    print(sum([char_score(char) for char in common_chars]))


def part_two(lines: List[str]):
    groups = []
    group = []
    for line in lines:
        group.append(line)
        if len(group) == 3:
            groups.append(group)
            group = []

    common_chars = [common_char(group) for group in groups]
    print(sum([char_score(char) for char in common_chars]))


if __name__ == "__main__":
    with open("./inputs/day_three.txt") as f:
        lines = f.read().splitlines()

    parsed_lines = [
        (line[: (len(line) // 2)], line[(len(line) // 2) :]) for line in lines
    ]

    part_one(parsed_lines)
    part_two(lines)
