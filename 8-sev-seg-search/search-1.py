#! /bin/python3


def ez_digits(inputs: list):
    patterns = [pattern[0].split() for pattern in inputs]

    displays = [display[1].split() for display in inputs]

    displays_joined = []
    for display in displays:
        displays_joined += display

    ez = [len(display) for display in displays_joined if len(display) in [2, 3, 4, 7]]

    return len(ez)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip().split('|') for line in file]

    print(ez_digits(values))
