#! /bin/python3

from timeit import default_timer as timer
from datetime import timedelta

def prod(list):
    return list[0] * list[1] * list[2]


def where_my_basins_at(start_x, start_y, tubes, traversed_locations):
    size = 1
    traversed_locations[start_y][start_x] = True

    traverse_left = start_x - 1
    if traverse_left >= 0:
        if not traversed_locations[start_y][traverse_left] and tubes[start_y][traverse_left] < 9:
            size += where_my_basins_at(traverse_left, start_y, tubes, traversed_locations)

    traverse_right = start_x + 1
    if traverse_right < len(tubes[start_y]):
        if not traversed_locations[start_y][traverse_right] and tubes[start_y][traverse_right] < 9:
            size += where_my_basins_at(traverse_right, start_y, tubes, traversed_locations)

    traverse_up = start_y - 1
    if traverse_up >= 0:
        if not traversed_locations[traverse_up][start_x] and tubes[traverse_up][start_x] < 9:
            size += where_my_basins_at(start_x, traverse_up, tubes, traversed_locations)

    traverse_down = start_y + 1
    if traverse_down < len(tubes):
        if not traversed_locations[traverse_down][start_x] and tubes[traverse_down][start_x] < 9:
            size += where_my_basins_at(start_x, traverse_down, tubes, traversed_locations)

    return size


def smoke_detector(inputs: list):
    tubes = [[int(character) for character in line] for line in inputs]
    traversed_locations = [[False] * (len(tubes[0])) for _ in range(len(tubes))]

    size = []

    for y in range(len(tubes)):
        for x in range(len(tubes[y])):
            lowpoint = True
            if y > 0:
                if tubes[y - 1][x] <= tubes[y][x]:
                    lowpoint = False

            if y < len(tubes) - 1:
                if tubes[y + 1][x] <= tubes[y][x]:
                    lowpoint = False

            if x > 0:
                if tubes[y][x - 1] <= tubes[y][x]:
                    lowpoint = False

            if x < len(tubes[y]) - 1:
                if tubes[y][x + 1] <= tubes[y][x]:
                    lowpoint = False

            if lowpoint:
                size.append(where_my_basins_at(x, y, tubes, traversed_locations))

    size.sort()

    return prod(size[-3:])


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    start_time = timer()

    print(smoke_detector(values))

    end_time = timer()

    print(f'time: {timedelta(seconds=end_time - start_time)}')
