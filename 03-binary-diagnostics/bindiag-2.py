#! /bin/python3

def most_common(values: list) -> int:
    return round(sum(values) / len(values) + 0.00001)


def get_rating(values: list, ox: bool) -> int:
    for i in range(len(values[0])):
        mcv = most_common([int(bit[i]) for bit in values])
        if ox:
            values = [value for value in values if int(value[i]) == mcv]
        else:
            values = [value for value in values if int(value[i]) != mcv]

        if len(values) == 1:
            return int(values[0], 2)

    return int(values[0], 2)


def diag_lsr(values: list) -> str:
    ox_rating = get_rating(values, True)
    scrub_rating = get_rating(values, False)
    return str(ox_rating * scrub_rating)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(diag_lsr(values))
