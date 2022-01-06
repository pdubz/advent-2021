#! /bin/python3

from copy import deepcopy


def cucumove(map):
    moved = False
    new_map = deepcopy(map)
    for y in range(len(map)):
        for x in range(len(map[y])):
            next_x = x + 1 if x + 1 < len(map[y]) else 0
            if map[y][x] == '>' and map[y][next_x] == '.':
                new_map[y][next_x] = '>'
                new_map[y][x] = '.'
                moved = True

    map = new_map

    new_map = deepcopy(map)
    for y in range(len(map)):
        next_y = y + 1 if y + 1 < len(map) else 0
        for x in range(len(map[y])):
            if map[y][x] == 'v' and map[next_y][x] == '.':
                new_map[next_y][x] = 'v'
                new_map[y][x] = '.'
                moved = True

    return moved, new_map


def print_map(lines):
    for y in range(len(lines)):
        for x in range(len(lines[0])):
            print(lines[y][x], end='')
        print()


def cucumber(input):
    iterations = 0
    while True:
        moved, input = cucumove(input)
        iterations += 1

        if not moved:
            break

    return iterations


if __name__ == '__main__':
    with open('input.txt') as file:
        values = []
        for line in file:
            values.append(list(line.strip()))
    print(cucumber(values))
