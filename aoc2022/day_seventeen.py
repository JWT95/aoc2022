SQUARE = {(2, 3), (2, 4), (3, 3), (3, 4)}
PLUS = {(3, 3), (2, 4), (3, 4), (4, 4), (3, 5)}
ELL = {(2, 3), (3, 3), (4, 3), (4, 4), (4, 5)}
VLINE = {(2, 3), (2, 4), (2, 5), (2, 6)}
HLINE = {(2, 3), (3, 3), (4, 3), (5, 3)}
SHAPES = [HLINE, PLUS, ELL, VLINE, SQUARE]

if __name__ == "__main__":
    with open("./inputs/day_seventeen.txt") as f:
        lines = f.read().splitlines()

    line = lines[0]

    rocks = {(i, 0) for i in range(1, 8)}
    wind_index = 0
    for i in range(100000000):
        height = max([rock[1] for rock in rocks])

        if i % 1000 == 0:
            # Get rid of anything below 100 max height
            print(i, height)
            rocks = {rock for rock in rocks if rock[1] > height - 1000}
        if i % 5 == 0 and wind_index % len(line) == 7:
            print("loop", i, height)
        if (i - 1715) % 1720 == 1445:
            print("1445", i, height)

        # Release the rock from the top of the pile
        height = max([rock[1] for rock in rocks])

        # Find the shape to apply and the direction to apply
        shape = SHAPES[i % 5]

        # Put shape in the right place
        shape = {(point[0] + 1, point[1] + height + 1) for point in shape}

        for j in range(1000):
            # Apply the wind direction
            direction = line[wind_index % len(line)]
            wind_index += 1
            if direction == "<":
                new_shape = {(point[0] - 1, point[1]) for point in shape}
            else:
                new_shape = {(point[0] + 1, point[1]) for point in shape}

            for point in new_shape:
                if point[0] <= 0 or point[0] >= 8 or point in rocks:
                    new_shape = shape
                    break

            shape = new_shape

            # Go down one
            new_shape = {(point[0], point[1] - 1) for point in shape}
            need_to_stop = False
            for point in new_shape:
                if point in rocks:
                    need_to_stop = True
                    break

            if need_to_stop:
                # We're done
                for point in shape:
                    rocks.add(point)

                break
            else:
                shape = new_shape

    print(max(rock[1] for rock in rocks))

    # The cycle repeats therefore it will be
    a = 1000000000000 - 1715 + 1445 + 2309
    2685 + 1570930227594 + 2303
