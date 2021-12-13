#! /bin/python3

def print_octos(octos):
    for y in range(len(octos)):
        for x in range(len(octos[y])):
            print(octos[y][x], end='')
        print()


def flash(x, y, octos, flashed):
    flashes = 0
    if x < 0 or y < 0 or x > len(octos[0]) - 1 or y > len(octos) - 1:
        return flashes

    if not flashed[y][x]:
        if octos[y][x] < 9:
            octos[y][x] += 1
        else:
            octos[y][x] = 0
            flashes += 1
            flashed[y][x] = True
            flashes += flash(x - 1, y - 1, octos, flashed)
            flashes += flash(x, y - 1, octos, flashed)
            flashes += flash(x + 1, y - 1, octos, flashed)
            flashes += flash(x + 1, y, octos, flashed)
            flashes += flash(x + 1, y + 1, octos, flashed)
            flashes += flash(x, y + 1, octos, flashed)
            flashes += flash(x - 1, y + 1, octos, flashed)
            flashes += flash(x - 1, y, octos, flashed)

    return flashes


def octo(inputs: list):
    flashes = 0
    for iteration in range(100):
        flashed = [[False] * len(inputs[0]) for i in range(len(inputs))]
        for y in range(len(inputs)):
            for x in range(len(inputs[y])):
                flashes += flash(x, y, inputs, flashed)

    return flashes


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [[int(character) for character in line.strip()] for line in file]

    print(octo(values))
