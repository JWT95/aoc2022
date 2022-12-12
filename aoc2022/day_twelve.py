from dijkstar import Graph, find_path


def connecting_points(point, points):
    connecting_points = []
    for i, j in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
        neighbour = (point[0] + i, point[1] + j)
        if neighbour in points:
            if points[neighbour] - points[point] <= 1:
                connecting_points.append(neighbour)

    return connecting_points


if __name__ == "__main__":
    with open("./inputs/day_twelve.txt") as f:
        lines = f.read().splitlines()

    # Let's create our set of points
    points = dict()
    for y in range(len(lines)):
        for x in range(len(lines[1])):
            value = ord(lines[y][x])
            if 97 <= value <= 122:
                points[(x, y)] = value
            elif lines[y][x] == "S":
                points[(x, y)] = 97
                start = (x, y)
            elif lines[y][x] == "E":
                points[(x, y)] = 122
                end = (x, y)
            else:
                print(lines[y][x])
                raise Exception

    graph = Graph()
    for y in range(len(lines)):
        for x in range(len(lines[1])):
            for neighbour in connecting_points((x, y), points):
                graph.add_edge((x, y), neighbour, 1)

    smallest_path = 100000
    for point in [point for (point, value) in points.items() if value == 97]:
        try:
            size = len(find_path(graph, point, end).edges)
            if size < smallest_path:
                smallest_path = size
        except Exception as e:
            continue

    print(smallest_path)
