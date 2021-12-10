#! /bin/python3

import statistics


def crabber(inputs: list):
    crabs = [int(item) for item in inputs]

    optimal = int(statistics.median(crabs))

    return sum([abs(distance - optimal) for distance in crabs])


if __name__ == '__main__':
    with open('input.txt') as file:
        values = file.readline().split(',')

    print(crabber(values))
