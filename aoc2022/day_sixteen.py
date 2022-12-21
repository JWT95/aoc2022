from dijkstar import Graph, find_path
from itertools import combinations


def find_max_walk_single(start, points, valves, walk_so_far, steps_left):
    neighbors = points[start]

    # Consider all the options
    # Never go back to one already visited
    max_walk = calculate_score(walk_so_far, valves)
    if len(walk_so_far) == len(points):
        return max_walk
    for neighbor in [
        neighbor
        for neighbor in neighbors
        if neighbor[0] not in walk_so_far.keys() and neighbor[0] in points.keys()
    ]:
        if neighbor[1] < steps_left:
            walk = find_max_walk_single(
                neighbor[0],
                points,
                valves,
                dict({neighbor[0]: steps_left - neighbor[1]}, **walk_so_far),
                steps_left - neighbor[1],
            )
            max_walk = max(walk, max_walk)

    return max_walk


def calculate_score(walk, valves):
    return sum([when * valves[key][0] for key, when in walk.items()])


# Do the same but now kick off two sets
def find_max_walk_double(
    start_one, start_two, points, valves, walk_so_far, steps_left, steps_right
):
    neighbors_left = points[start_one]
    neighbors_right = points[start_two]

    # Consider the next places to visit for both
    max_walk = calculate_score(walk_so_far, valves)

    for neighbor in [
        neighbor for neighbor in neighbors_left if neighbor[0] not in walk_so_far.keys()
    ]:
        if neighbor[1] < steps_left:
            walk = find_max_walk_double(
                neighbor[0],
                start_two,
                points,
                valves,
                dict({neighbor[0]: steps_left - neighbor[1]}, **walk_so_far),
                steps_left - neighbor[1],
                steps_right,
            )
            max_walk = max(walk, max_walk)

    for neighbor in [
        neighbor
        for neighbor in neighbors_right
        if neighbor[0] not in walk_so_far.keys()
    ]:
        if neighbor[1] < steps_right:
            walk = find_max_walk_double(
                start_one,
                neighbor[0],
                points,
                valves,
                dict({neighbor[0]: steps_right - neighbor[1]}, **walk_so_far),
                steps_left,
                steps_right - neighbor[1],
            )
            max_walk = max(walk, max_walk)

    # Consider all the options
    # Never go back to one already visited
    # for neighbor_left in [neighbor for neighbor in neighbors_left if neighbor[0] not in walk_so_far.keys()]:
    #     for neighbor_right in [neighbor for neighbor in neighbors_right if neighbor[0] not in walk_so_far.keys()]:
    #         if neighbor_left != neighbor_right:
    #             if neighbor_left[1] < steps_left and neighbor_right[1] < steps_right:
    #                 walk = find_max_walk_double(neighbor_left[0], neighbor_right[0], points, valves, dict({neighbor_left[0]: steps_left-neighbor_left[1], neighbor_right[0]: steps_right-neighbor_right[1]}, **walk_so_far), steps_left-neighbor_left[1], steps_right-neighbor_right[1])
    #                 max_walk = max(walk, max_walk)
    #             elif neighbor_left[1] < steps_left:
    #                 walk = find_max_walk_single(neighbor_left[0], points, valves, dict({neighbor_left[0]: steps_left-neighbor_left[1]}, **walk_so_far), steps_left-neighbor_left[1])
    #                 max_walk = max(walk, max_walk)
    #             elif neighbor_right[1] < steps_right:
    #                 walk = find_max_walk_single(neighbor_right[0], points, valves, dict({neighbor_right[0]: steps_right-neighbor_right[1]}, **walk_so_far), steps_right-neighbor_right[1])
    #                max_walk = max(walk, max_walk)

    return max_walk


if __name__ == "__main__":
    with open("./inputs/day_sixteen.txt") as f:
        lines = f.read().splitlines()

    valves = dict()
    for line in lines:
        splitline = line.split()
        name = splitline[1]
        rate = splitline[4]
        rate = int(rate.split("=")[1].rstrip(";"))
        neighbors = splitline[9:]
        neighbors = [valve.rstrip(",") for valve in neighbors]
        valves[name] = (rate, neighbors)

    # Make a graph of stuff and then filter down to just the good ones
    graph = Graph()
    for name, valve in valves.items():
        for neighbor in valve[1]:
            graph.add_edge(name, neighbor, 1)

    # Get the valves with non-zero value or AA
    high_value_items_pre = {name for name, value in valves.items() if (value[0] > 0)}
    high_value_items = {"AA", *high_value_items_pre}

    # Now form a new set with the points and their distances from other stuff
    points = dict()
    for point in high_value_items:
        points[point] = []
        for neighbor in [
            neighbor for neighbor in high_value_items if point != neighbor
        ]:
            points[point].append(
                (neighbor, len(find_path(graph, point, neighbor).edges) + 1)
            )

    print(find_max_walk_single("AA", points, valves, dict(), 30))

    print(points)

    # Choose a partition of the interesting points
    print(len(high_value_items_pre))
    max_score = 0
    for combination in combinations(high_value_items_pre, 8):
        set_a = dict({"AA": points["AA"]}, **{a: points[a] for a in combination})
        set_b = dict(
            {"AA": points["AA"]},
            **{b: points[b] for b in high_value_items_pre if b not in set_a}
        )

        walk_a = find_max_walk_single("AA", set_a, valves, dict(), 26)
        walk_b = find_max_walk_single("AA", set_b, valves, dict(), 26)

        if walk_a + walk_b > max_score:
            max_score = walk_a + walk_b
            print(walk_a + walk_b)
