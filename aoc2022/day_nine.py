if __name__ == "__main__":
    with open("./inputs/day_nine.txt") as f:
        lines = f.read().splitlines()

    # We don't need a grid
    # Just a set of tuples

    head_square = (0, 0)
    squares = [(0, 0) for i in range(9)]
    tail_squares = {(0, 0)}

    for line in lines:
        split_line = line.split()
        for step in range(int(split_line[1])):
            if split_line[0] == "R":
                head_square = (head_square[0] + 1, head_square[1])
            if split_line[0] == "L":
                head_square = (head_square[0] - 1, head_square[1])
            if split_line[0] == "U":
                head_square = (head_square[0], head_square[1] - 1)
            if split_line[0] == "D":
                head_square = (head_square[0], head_square[1] + 1)

            # Now update tail squares
            for i in range(9):
                if i == 0:
                    fore_square = head_square
                else:
                    fore_square = squares[i - 1]

                # Now update tail squares
                distance = abs(fore_square[0] - squares[i][0]) + abs(
                    fore_square[1] - squares[i][1]
                )

                if distance > 2:
                    if squares[i][1] < fore_square[1]:
                        squares[i] = (squares[i][0], squares[i][1] + 1)
                    if squares[i][1] > fore_square[1]:
                        squares[i] = (squares[i][0], squares[i][1] - 1)
                else:
                    if squares[i][1] < fore_square[1] - 1:
                        squares[i] = (squares[i][0], squares[i][1] + 1)
                    if squares[i][1] > fore_square[1] + 1:
                        squares[i] = (squares[i][0], squares[i][1] - 1)

                if distance > 2:
                    if squares[i][0] < fore_square[0]:
                        squares[i] = (squares[i][0] + 1, squares[i][1])
                    if squares[i][0] > fore_square[0]:
                        squares[i] = (squares[i][0] - 1, squares[i][1])
                else:
                    if squares[i][0] < fore_square[0] - 1:
                        squares[i] = (squares[i][0] + 1, squares[i][1])
                    if squares[i][0] > fore_square[0] + 1:
                        squares[i] = (squares[i][0] - 1, squares[i][1])

            tail_squares.add((squares[8][0], squares[8][1]))

    print(len(tail_squares))
