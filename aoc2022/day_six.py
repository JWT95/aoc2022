if __name__ == "__main__":
    with open("./inputs/day_six.txt") as f:
        lines = f.read()

    latest_chars = [lines[i] for i in range(14)]
    position = 15

    while True:
        # Get the character at the position
        latest_chars.pop(0)
        latest_chars.append(lines[position])

        # Check for set uniqueness
        if len(set(latest_chars)) == 14:
            break
        else:
            position += 1

    print(position + 1)
