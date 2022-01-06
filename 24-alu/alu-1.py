#! /bin/python3

# Each block in the input contains these magic constants
CONSTANTS = {
    'x': [12, 11, 10, 10, -16, 14, 12, -4, 15, -7, -8, -4, -15, -8],
    'y': [6, 12, 5, 10, 7, 0, 4, 12, 14, 13, 10, 11, 9, 9],
    'z': [1, 1, 1, 1, 26, 1, 1, 26, 1, 26, 26, 26, 26, 26]
}


def check_serial(input):
    final = 0
    for w, const_x, const_y, const_z in zip(input, CONSTANTS['x'], CONSTANTS['y'], CONSTANTS['z']):
        working = final // const_z
        if w == final % 26 + const_x:
            final = working
        else:
            final = 26 * working + w + const_y
    return final == 0


def reversed_check(const_x, const_y, const_z, z, w):
    zs = []
    x = z - w - const_y
    if x % 26 == 0:
        zs.append(x // 26 * const_z)
    if 0 <= w - const_x < 26:
        working_z = z * const_z
        zs.append(w - const_x + working_z)

    return zs


def solve():
    potentials = {0}
    result = {}
    # Work backwards through each block of instructions finding the maximum value for the block that will set z to 0
    for const_x, const_y, const_z in zip(CONSTANTS['x'][::-1], CONSTANTS['y'][::-1], CONSTANTS['z'][::-1]):
        new_potentials = set()
        for w, z in [(w, z) for w in range(1, 10) for z in potentials]:
            for working_z in reversed_check(const_x, const_y, const_z, z, w):
                new_potentials.add(working_z)
                result[working_z] = (w,) + result.get(z, ())
        potentials = new_potentials

    if check_serial(result[0]):
        return ''.join(str(digit) for digit in result[0])
    else:
        return 'yikes'


if __name__ == '__main__':
    print(solve())
