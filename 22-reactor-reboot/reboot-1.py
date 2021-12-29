#! /bin/python3

from re import search
from collections import defaultdict


def inbounds(x1, x2, y1, y2, z1, z2):
    return -50 <= x1 <= x2 <= 50 and -50 <= y1 <= y2 <= 50 and -50 <= z1 <= z2 <= 50


def reboot(input):
    reactor = defaultdict(int)
    for step in input:
        command = step[0]
        x1, x2, y1, y2, z1, z2 = [int(coordinate) for coordinate in step[1:]]
        if inbounds(x1, x2, y1, y2, z1, z2):
            for x in range(x1, x2 + 1):
                for y in range(y1, y2 + 1):
                    for z in range(z1, z2 + 1):
                        reactor[(x, y, z)] = 1 if command == 'on' else 0

    return len([cube for cube in reactor.values() if cube == 1])


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [search('(on|off)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)..=(-?\\d+)..(-?\\d+)', line).groups()
                  for line in file]

    print(reboot(values))
