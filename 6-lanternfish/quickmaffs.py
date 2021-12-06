#! /bin/python3

import numpy as np


def turn_me_lan(inputs: list):
    fishies = [int(item) for item in inputs]

    initial_fishies = np.array([fishies.count(day) for day in range(9)])

    fishy_model_matrix = np.array(
        [
            [0, 1, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 1, 0, 0],
            [1, 0, 0, 0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0]
        ]
    )

    fishy_power = np.linalg.matrix_power(fishy_model_matrix, 256)

    return fishy_power.dot(initial_fishies).sum()


if __name__ == '__main__':
    with open('input.txt') as file:
        values = file.readline().split(',')

    print(turn_me_lan(values))
