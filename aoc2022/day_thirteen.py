import functools


def compare_items(a, b) -> int:
    if isinstance(a, int) and isinstance(b, int):
        if a < b:
            return -1
        elif a == b:
            return 0
        else:
            return 1

    if isinstance(a, int) and isinstance(b, list):
        return compare_items([a], b)

    if isinstance(a, list) and isinstance(b, int):
        return compare_items(a, [b])

    if isinstance(a, list) and isinstance(b, list):
        a = [a for a in a]
        b = [b for b in b]
        if len(a) < len(b):
            a.extend([-1 for _ in range(len(b) - len(a))])
        elif len(b) < len(a):
            b.extend([-1 for _ in range(len(a) - len(b))])

        for i in range(len(a)):
            compare_item = compare_items(a[i], b[i])

            if compare_item != 0:
                return compare_item

        return 0


if __name__ == "__main__":
    with open("./inputs/day_thirteen.txt") as f:
        lines = f.read().splitlines()

    # lines.append("")
    pairs = []
    left = None
    right = None
    # for line in lines:
    #     if line:
    #         if left != None:
    #             right = eval(line)
    #         else:
    #             left = eval(line)
    #     else:
    #         pairs.append((left, right))
    #         left, right = (None, None)

    items = [eval(line) for line in lines if line]
    items.extend([[[2]], [[6]]])

    # right_sized_pairs = 0
    # for i in range(len(pairs)):
    #     if compare_items(pairs[i][0], pairs[i][1]) == -1:
    #         print("Match: ", i + 1)
    #         right_sized_pairs += i + 1
    #     else:
    #         print("No match: ", i + 1)

    # print(right_sized_pairs)

    sorted_items = sorted(items, key=functools.cmp_to_key(compare_items))

    print((1 + sorted_items.index([[2]])) * (1 + sorted_items.index([[6]])))
