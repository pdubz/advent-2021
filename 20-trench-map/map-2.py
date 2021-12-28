#! /bin/python3

from copy import deepcopy


def print_image(image):
    for line in image:
        for character in line:
            print(character, end='')
        print()


def get_value(x, y, image):
    value = ''
    for y_index in range(y - 1, y + 2):
        for x_index in range(x - 1, x + 2):
            value += '0' if image[y_index][x_index] == '.' else '1'

    return int(value, 2)


def embiggen(image, infinite_character):
    top = [infinite_character for i in range(len(image[0]) + 4)]
    bot = [infinite_character for i in range(len(image[0]) + 4)]

    for i, line in enumerate(image):
        image[i] = [infinite_character, infinite_character] + line + [infinite_character, infinite_character]

    image.insert(0, top.copy())
    image.insert(0, top.copy())
    image.append(bot.copy())
    image.append(bot.copy())


def enhance(algorithm, image, rounds):
    infinite_character = '.'
    for round in range(rounds):
        new_image = deepcopy(image)
        embiggen(image, infinite_character)
        infinite_character = '#' if infinite_character == '.' else '.'
        embiggen(new_image, infinite_character)
        for y in range(1, len(new_image) - 1):
            for x in range(1, len(new_image[0]) - 1):
                new_image[y][x] = algorithm[get_value(x, y, image)]

        image = new_image

    ones = 0
    for row in image:
        for character in row:
            if character == '#':
                ones += 1

    return ones


if __name__ == '__main__':
    values = []
    with open('input.txt') as file:
        algo = file.readline().strip()
        file.readline()
        input = [list(line.strip()) for line in file]

    print(enhance(algo, input, 50))
