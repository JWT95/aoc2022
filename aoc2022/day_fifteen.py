def points_distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


LINE = 2000000

if __name__ == "__main__":
    with open("./inputs/day_fifteen.txt") as f:
        lines = f.read().splitlines()

    sensors = dict()
    beacons = set()

    for line in lines:
        numbers = line.split("=")
        x = int(numbers[1].split(",")[0])
        y = int(numbers[2].split(":")[0])

        a = int(numbers[3].split(",")[0])
        b = int(numbers[4])

        beacons.add((a, b))
        sensors[(x, y)] = (a, b)

    # For each point get the distance between it and the beacon
    overall_banned_points = dict()
    for i in range(-2000000, 2000000):
        banned_points = set()

        line = LINE + i
        for sensor, beacon in sensors.items():
            distance = points_distance(sensor, beacon)

            # Get distance between point and line
            distance_line = points_distance(sensor, (sensor[0], line))

            # Then for each point between that and the total distance, add that point to the thing
            if distance_line <= distance:
                banned_points.add(
                    (
                        (max(sensor[0] - (distance - distance_line), 0)),
                        min(sensor[0] + (distance - distance_line), 2 * LINE),
                    )
                )

        # Consolidate ranges
        ranges = sorted(banned_points)
        final_ranges = []
        current_max = 0
        for i in range(len(ranges) - 1):
            current_max = max(current_max, ranges[i][1])
            if current_max < ranges[i + 1][0] - 1:
                final_ranges = [
                    (ranges[0][0], current_max),
                    (ranges[i + 1][0], ranges[-1][1]),
                ]

        if not final_ranges:
            final_ranges = [(ranges[0][0], ranges[-1][1])]

        if len(final_ranges) == 2:
            point = final_ranges[0][1] + 1
            print(4000000 * point + line)
