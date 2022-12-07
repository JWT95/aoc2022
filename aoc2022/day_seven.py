from typing import Dict, Tuple


def get_under_size_of_directory(directory: Dict) -> int:
    # The under size of a directory is the sum of the undersizes of this directory
    # Plus the size of this directory if it is less than 100000
    size = get_size_of_directory(directory)
    under_size = 0

    for key, item in directory.items():
        if isinstance(item, int):
            pass
        elif key == "..":
            pass
        else:
            under_size += get_under_size_of_directory(item)

    if size <= 100000:
        return size + under_size
    else:
        return under_size


def get_size_of_directory(directory: Dict) -> int:
    size = 0
    for key, item in directory.items():
        if isinstance(item, int):
            size += item
        elif key == "..":
            pass
        else:
            size += get_size_of_directory(item)

    return size


def smallest_directory_under_size(directory: Dict, min_size: int) -> int:
    size = get_size_of_directory(directory)
    candidate_sizes = [size]
    for key, item in directory.items():
        if isinstance(item, int):
            size += item
        elif key == "..":
            pass
        else:
            candidate_sizes.append(smallest_directory_under_size(item, min_size))

    for size in sorted(candidate_sizes):
        if size >= min_size:
            return size

    return 0


if __name__ == "__main__":
    with open("./inputs/day_seven.txt") as f:
        lines = f.read().splitlines()

    current_directory = dict()
    directory_struct = {"/": current_directory}

    for line in lines[1:]:
        splitline = line.split(" ")
        if splitline[0] == "$":
            # We have a command
            if splitline[1] == "cd":
                current_directory = current_directory[splitline[2]]
        else:
            # We have a file or directory
            if splitline[0] == "dir":
                # Add to the current directory
                current_directory[splitline[1]] = {"..": current_directory}
            else:
                current_directory[splitline[1]] = int(splitline[0])

    print(get_under_size_of_directory(directory_struct))

    size_needed = get_size_of_directory(directory_struct) - 40000000

    # We want to find the smallest directory over size_needed
    print(smallest_directory_under_size(directory_struct, size_needed))
