def range_from_str(string: str) -> range:
    split_string = string.split("-")
    return range(int(split_string[0]), int(split_string[1]) + 1)


def seq_is_superset(seq_one, seq_two) -> bool:
    return seq_one[0] <= seq_two[0] and seq_one[-1] >= seq_two[-1]


def seq_overlaps(seq_one, seq_two) -> bool:
    return (
        seq_two[0] <= seq_one[0] <= seq_two[-1]
        or seq_one[0] <= seq_two[0] <= seq_one[-1]
    )


if __name__ == "__main__":
    with open("./inputs/day_four.txt") as f:
        lines = f.read().splitlines()

    pairs = [
        (range_from_str(strings[0]), range_from_str(strings[1]))
        for strings in [line.split(",") for line in lines]
    ]

    superset_pairs = [
        (x, y) for (x, y) in pairs if (seq_is_superset(x, y) or seq_is_superset(y, x))
    ]

    overlap_pairs = [(x, y) for (x, y) in pairs if seq_overlaps(x, y)]

    print(len(superset_pairs))
    print(len(overlap_pairs))
