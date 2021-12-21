#! /bin/python3

class Snail:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    @classmethod
    def parse(cls, value, index=0):
        if value[index].isdigit():
            return cls(int(value[index])), index + 1
        snail = cls()
        snail.left, index = cls.parse(value, index + 1)
        snail.right, index = cls.parse(value, index + 1)
        return snail, index + 1

    def __str__(self):
        if self.value is not None:
            return str(self.value)
        return f'[{self.left}, {self.right}]'

    def replace(self, first, second):
        if self.left == first:
            self.left = second
        else:
            self.right = second

    def flatten(self, flattened):
        if self.value is not None:
            flattened.append(self)
        if self.left:
            self.left.flatten(flattened)
        if self.right:
            self.right.flatten(flattened)
        return flattened

    def magnitude(self):
        if self.value is not None:
            return self.value
        return 3 * self.left.magnitude() + 2 * self.right.magnitude()


def split(snail, depth, parent):
    if snail.value is not None:
        if snail.value < 10:
            return False
        parent.replace(snail, Snail(left=Snail(int(snail.value / 2)), right=Snail(round((snail.value / 2) + 0.00001))))
        return True
    if split(snail.left, depth + 1, snail):
        return True
    return split(snail.right, depth + 1, snail)


def explode(snail, flat_snail, depth, parent):
    if snail.value is not None:
        return False
    if depth == 4:
        index = flat_snail.index(snail.left)
        if index > 0:
            flat_snail[index - 1].value += snail.left.value
        if index < len(flat_snail) - 2:
            flat_snail[index + 2].value += snail.right.value
        parent.replace(snail, Snail(0))
        return True
    if explode(snail.left, flat_snail, depth + 1, snail):
        return True
    return explode(snail.right, flat_snail, depth + 1, snail)


def add(first, second):
    snail = Snail(left=first, right=second)
    action_occurred = True
    while action_occurred:
        if not explode(snail, snail.flatten([]), 0, None):
            if not split(snail, 0, None):
                action_occurred = False

    return snail


def snail_math(input):
    number = Snail.parse(input[0])[0]
    for next_number in input[1:]:
        number = add(number, Snail.parse(next_number)[0])

    return number.magnitude()


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(snail_math(values))
