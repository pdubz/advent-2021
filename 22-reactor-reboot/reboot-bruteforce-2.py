#! /usr/bin/pypy3

from re import search


def reboot(input):
    steps = []
    xs = []
    ys = []
    zs = []
    for step in input:
        command = step[0]
        x1, x2, y1, y2, z1, z2 = [int(coordinate) for coordinate in step[1:]]
        steps.append((command == "on", (x1, x2), (y1, y2), (z1, z2)))
        xs.append(x1)
        xs.append(x2 + 1)
        ys.append(y1)
        ys.append(y2 + 1)
        zs.append(z1)
        zs.append(z2 + 1)

    steps.reverse()
    xs.sort()
    ys.sort()
    zs.sort()

    on = 0

    for x1, x2 in zip(xs, xs[1:]):
        print(f'Processing: {x1} {x2}')
        x_steps = [(command, x, y, z) for command, x, y, z in steps if x[0] <= x1 <= x[1]]
        for y1, y2 in zip(ys, ys[1:]):
            y_steps = [(command, x, y, z) for command, x, y, z in x_steps if y[0] <= y1 <= y[1]]
            for z1, z2 in zip(zs, zs[1:]):
                if next((command for command, x, y, z in y_steps if z[0] <= z1 <= z[1]), False):
                    on += (x2 - x1) * (y2 - y1) * (z2 - z1)

    return on


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [search('(on|off)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)', line).groups()
                  for line in file]

    print(reboot(values))
