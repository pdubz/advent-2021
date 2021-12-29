#! /bin/python3

from functools import lru_cache


@lru_cache(maxsize=None)
def show_me_what_you_dirac(pos1, pos2, score1, score2):
    if score1 >= 21:
        return 1, 0
    if score2 >= 21:
        return 0, 1

    total_wins1 = 0
    total_wins2 = 0

    for sum, universes in dice_permutations:
        new_pos1 = (pos1 + sum) % 10
        new_score1 = score1 + new_pos1 + 1
        wins2, wins1 = show_me_what_you_dirac(pos2, new_pos1, score2, new_score1)
        total_wins1 += wins1 * universes
        total_wins2 += wins2 * universes

    return total_wins1, total_wins2


# from collections import defaultdict
# dice_permutations = defaultdict(int)
# for roll1 in range(1, 4):
#     for roll2 in range(1, 4):
#         for roll3 in range(1, 4):
#             dice_permutations[sum([roll1, roll2, roll3])] += 1
dice_permutations = [(3, 1), (4, 3), (5, 6), (6, 7), (7, 6), (8, 3), (9, 1)]


def rollin(p1, p2):
    p1_wins, p2_wins = show_me_what_you_dirac(p1, p2, 0, 0)

    return max(p1_wins, p2_wins)


if __name__ == '__main__':
    with open('input.txt') as file:
        # Positions are all shifted by -1 because the board is 1 indexed instead of 0 indexed...
        p1_start = int(file.readline().split()[-1]) - 1
        p2_start = int(file.readline().split()[-1]) - 1

    print(rollin(p1_start, p2_start))
