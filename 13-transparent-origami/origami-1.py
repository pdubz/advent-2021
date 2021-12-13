#! /bin/python3

def print_origami(paper):
    for y in range(len(paper)):
        for x in range(len(paper[y])):
            print(paper[y][x], end='')
        print()


def ori_my_gami(coordinates: list, folds: list):
    for i, (x, y) in enumerate(coordinates):
        if folds[0][0] == 'x':
            coordinates[i] = (2 * abs(folds[0][1] - x), y)
        if folds[0][0] == 'y':
            coordinates[i] = (x, 2 * abs(folds[0][1] - y))

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
