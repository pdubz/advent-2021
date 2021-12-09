#! /bin/python3


def smoke_detector(inputs: list):
    tubes = [[int(character) for character in line] for line in inputs]

    risk = 0

    for y in range(len(tubes)):
        for x in range(len(tubes[y])):
            lowpoint = True
            if y > 0:
                if tubes[y - 1][x] <= tubes[y][x]:
                    lowpoint = False

            if y < len(tubes) - 1:
                if tubes[y + 1][x] <= tubes[y][x]:
                    lowpoint = False

            if x > 0:
                if tubes[y][x - 1] <= tubes[y][x]:
                    lowpoint = False
            if x < len(tubes[y]) - 1:
                if tubes[y][x + 1] <= tubes[y][x]:
                    lowpoint = False

            if lowpoint:
                risk += tubes[y][x] + 1

    return risk


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(smoke_detector(values))
