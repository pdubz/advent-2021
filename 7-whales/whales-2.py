#! /bin/python3

import statistics


def ive_got_crabs(inputs: list):
    crabs = [int(item) for item in inputs]

    optimal = int(statistics.mean(crabs))

    return sum([int((abs(distance - optimal) * (abs(distance - optimal) + 1)) / 2) for distance in crabs])


if __name__ == '__main__':
    with open('input.txt') as file:
        values = file.readline().split(',')

    print(ive_got_crabs(values))
