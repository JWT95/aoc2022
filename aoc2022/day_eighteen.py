from dijkstar import Graph, find_path

movements = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]


def free(point, points) -> int:
    count = 0

    if (point[0] + 1, point[1], point[2]) not in points:
        count += 1

    if (point[0] - 1, point[1], point[2]) not in points:
        count += 1

    if (point[0], point[1] + 1, point[2]) not in points:
        count += 1

    if (point[0], point[1] - 1, point[2]) not in points:
        count += 1

    if (point[0], point[1], point[2] + 1) not in points:
        count += 1

    if (point[0], point[1], point[2] - 1) not in points:
        count += 1

    return count


def reachable(point, points, graph) -> int:
    count = 0

    for movement in movements:
        candidate = tuple(point[i] + movement[i] for i in range(3))

        if candidate not in points:
            try:
                find_path(graph, candidate, (-1, -1, -1))
                count += 1
            except:
                pass

    return count


if __name__ == "__main__":
    with open("./inputs/day_eighteen.txt") as f:
        lines = f.read().splitlines()

    points = set()
    for line in lines:
        points.add(tuple(int(a) for a in line.split(",")))

    count_free = 0
    for point in points:
        count_free += free(point, points)

    print(count_free)

    graph = Graph()
    for x in range(-1, 23):
        for y in range(-1, 23):
            for z in range(-1, 23):
                point = (x, y, z)
                if point not in points:
                    if (point[0] + 1, point[1], point[2]) not in points:
                        graph.add_edge(point, (point[0] + 1, point[1], point[2]), 1)

                    if (point[0] - 1, point[1], point[2]) not in points:
                        graph.add_edge(point, (point[0] - 1, point[1], point[2]), 1)

                    if (point[0], point[1] + 1, point[2]) not in points:
                        graph.add_edge(point, (point[0], point[1] + 1, point[2]), 1)

                    if (point[0], point[1] - 1, point[2]) not in points:
                        graph.add_edge(point, (point[0], point[1] - 1, point[2]), 1)

                    if (point[0], point[1], point[2] + 1) not in points:
                        graph.add_edge(point, (point[0], point[1], point[2] + 1), 1)

                    if (point[0], point[1], point[2] - 1) not in points:
                        graph.add_edge(point, (point[0], point[1], point[2] - 1), 1)

    print(sum([reachable(point, points, graph) for point in points]))
