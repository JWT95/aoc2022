if __name__ == "__main__":
    with open("./inputs/day_twenty.txt") as f:
        lines = f.read().splitlines()


    # Construct
    factor = 811589153
    points = {i: (i, factor*int(lines[i])) for i in range(len(lines))}
    print(points)

    start = [int(a) for a in lines]
    current_positions = [i for i in range(len(start))]

    # Rather than constantly resize an array we'll just keep track
    # of where a number has moved to
    for k in range(10):
        print(k)
        for i in range(len(start)):
            # Find the current position of the ith number
            position = 0
            for key, value in points.items():
                if value[0] == i:
                    position = key
                    break

            value = points[position]


            # Find the number to move
            new_position = (position + value[1]) % (len(start) -1)

            # Move everthing else
            no_to_move = new_position - position

            if no_to_move > 0:
                for j in range(no_to_move) :
                    points[(position+j)] = points[(position+j+1)]

            if no_to_move < 0:
                for j in range(-no_to_move):
                    points[(position-j)] = points[(position-j-1) ]

            # Move it by that many places
            points[new_position] = value

        print(points)


    # Find zero
    zero_pos = 0
    for key, value in points.items():
        if value[1] == 0:
            zero_pos = key
            break


    calc = 0
    for i in (1000, 2000, 3000):
        calc += points[(zero_pos+i) % len(start)][1]
        print(points[(zero_pos+i) % len(start)][1])

    print(calc)
