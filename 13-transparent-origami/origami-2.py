#! /bin/python3

def print_origami(paper):
    for y in range(len(paper)):
        for x in range(len(paper[y])):
            print(paper[y][x], end='')
        print()


def ori_my_gami(coordinates: list, folds: list):
    for axis, location in folds:
        for i, (x, y) in enumerate(coordinates):
            if axis == 'x' and x > location:
                coordinates[i] = (2 * location - x, y)
            if axis == 'y' and y > location:
                coordinates[i] = (x, 2 * location - y)

    width = max(x[0] for x in set(coordinates)) + 1
    height = max([y[1] for y in set(coordinates)]) + 1

    paper = [['.'] * width for y in range(height)]
    for x, y in set(coordinates):
        paper[y][x] = '#'
    print_origami(paper)

    return len(set(coordinates))


if __name__ == '__main__':
    with open('input.txt') as file:
        values = {}
        blank = False
        coord_inputs = []
        fold_inputs = []
        for line in file:
            if line.strip() == '':
                blank = True
                continue
            if not blank:
                x, y = line.strip().split(',')
                coord_inputs.append((int(x), int(y)))
            else:
                axis, location = line.strip().split('=')
                axis = axis[-1:]
                fold_inputs.append([axis, int(location)])

    print(ori_my_gami(coord_inputs, fold_inputs))
