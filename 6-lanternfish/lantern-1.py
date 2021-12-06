#! /bin/python3


def turn_me_lan(inputs: list):
    fishies = [int(item) for item in inputs]

    for _ in range(80):
        for i in range(len(fishies)):
            if fishies[i] == 0:
                fishies[i] = 6
                fishies.append(8)
            else:
                fishies[i] -= 1

    return len(fishies)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = file.readline().split(',')

    print(turn_me_lan(values))
