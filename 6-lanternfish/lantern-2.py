#! /bin/python3

# import numpy # uncomment for timing purposes vs O(log(n)) implementation


def turn_me_lan(inputs: list):
    fishies = [int(item) for item in inputs]

    fishy_counters = {
        0: fishies.count(0),
        1: fishies.count(1),
        2: fishies.count(2),
        3: fishies.count(3),
        4: fishies.count(4),
        5: fishies.count(5),
        6: fishies.count(6),
        7: fishies.count(7),
        8: fishies.count(8)
    }

    for i in range(256):
        fishy_counters = {
            0: fishy_counters[1],
            1: fishy_counters[2],
            2: fishy_counters[3],
            3: fishy_counters[4],
            4: fishy_counters[5],
            5: fishy_counters[6],
            6: fishy_counters[7] + fishy_counters[0],
            7: fishy_counters[8],
            8: fishy_counters[0]
        }

    return sum(fishy_counters.values())


if __name__ == '__main__':
    with open('input.txt') as file:
        values = file.readline().split(',')

    print(turn_me_lan(values))
