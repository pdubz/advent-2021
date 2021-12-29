#! /bin/python3

from re import search


def overlap(first, second):
    x1, y1, z1 = [min(first[i], second[i]) for i in range(1, 6, 2)]
    x2, y2, z2 = [max(first[i], second[i]) for i in range(0, 5, 2)]
    if x1 - x2 >= 0 and y1 - y2 >= 0 and z1 - z2 >= 0:
        return x2, x1, y2, y1, z2, z1
    return None


def reboot(input):
    on = 0
    counted = []
    for step in reversed(input):
        mode, cube = step[0], step[1:]
        x1, x2, y1, y2, z1, z2 = cube
        if mode == 'on':
            kill_cubes = []
            for overlapped in [overlap(counted_cube, cube) for counted_cube in counted]:
                if overlapped:
                    kill_cubes.append(('on', *overlapped))
            on += (x2 - x1 + 1) * (y2 - y1 + 1) * (z2 - z1 + 1)
            on -= reboot(kill_cubes)
        counted.append(cube)
    return on


if __name__ == '__main__':
    with open('input.txt') as file:
        values = []
        for line in file:
            value = search('(on|off)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)', line).groups()
            values.append((value[0], *[int(i) for i in value[1:]]))

    print(reboot(values))
