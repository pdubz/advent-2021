#! /bin/python3

def bit_flip(bits: list) -> list:
    for i in range(len(bits)):
        bits[i] = int(not bool(bits[i]))

    return bits


def diag(values: list) -> str:
    gamma = 0
    epsilon = 0

    if values:
        bits = [int(bit) for bit in values[0]]
        for binary_string in values[1:]:
            for i in range(len(binary_string)):
                bits[i] += int(binary_string[i])

        for i in range(len(bits)):
            bits[i] = round(bits[i] / len(values))

        gamma = int(''.join([str(bit) for bit in bits]), 2)
        epsilon = int(''.join([str(bit) for bit in bit_flip(bits)]), 2)

    return str(gamma * epsilon)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(diag(values))
