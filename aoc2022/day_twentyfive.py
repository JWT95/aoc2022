def parse_snafu(number):
    total = 0
    for i in range(len(number)):
        candidate = number[len(number) - 1 - i]
        if candidate == "-":
            candidate = -1
        elif candidate == "=":
            candidate = -2
        else:
            candidate = int(candidate)
        total += 5**i * candidate

    return total


def decimal_to_snafu(number):
    # While true we'll find the number mod 5 to the power and then be done
    value = ""
    for i in range(50):
        # Find the mod
        modulo = (number % (5 ** (i + 1))) // (5**i)
        if modulo == 4:
            modulo = -1
        elif modulo == 3:
            modulo = -2

        number = number - (modulo * 5**i)

        if modulo == -1:
            value = "-" + value
        elif modulo == -2:
            value = "=" + value
        else:
            value = str(modulo) + value

        if number == 0:
            return value


if __name__ == "__main__":
    with open("./inputs/day_twentyfive.txt") as f:
        lines = f.read().splitlines()

    total = sum([parse_snafu(line) for line in lines])
    converted = decimal_to_snafu(total)
    print(converted)
