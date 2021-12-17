#! /bin/python3

import re


def check_bounds(x, y, target):
    return target[0] <= x <= target[1] and target[2] <= y <= target[3]


def simulate(x_velocity, y_velocity, target):
    x, y = 0, 0
    positions = [(0, 0)]

    while x <= target[1] and y >= target[2]:
        x += x_velocity
        if x_velocity > 0:
            x_velocity -= 1
        y += y_velocity
        y_velocity -= 1
        positions.append((x, y))
        if check_bounds(x, y, target):
            return True, positions
    return False, positions


def get_max_y(simulations):
    max_y = 0
    for sim in simulations:
        for position in sim:
            if position[1] > max_y:
                max_y = position[1]
    return max_y


def probe_it(target: tuple):
    sims = []
    for x_vel in range(target[1]):
        for y_vel in range(-target[2], target[2], -1):
            sims.append(simulate(x_vel, y_vel, target))

    return get_max_y([position[1] for position in sims if position[0]])


if __name__ == '__main__':
    with open('input.txt') as file:
        value = file.readline().strip()

    x1, x2, y1, y2 = re.search('x=(-?\\d+)..(\\d+), y=(-?\\d+)..(-?\\d+)', value).groups()

    print(probe_it((int(x1), int(x2), int(y1), int(y2))))
