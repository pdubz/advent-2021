#! /bin/python3

from collections import Counter


def well_extend_my_polymer(polymer: str, rules: dict, iterations: int):
    for iteration in range(iterations):
        new_polymer = polymer[0:1]
        for location in range(len(polymer) - 1):
            block = polymer[location:location + 2]
            if block in rules:
                new_polymer += rules[block]
                new_polymer += polymer[location + 1:location + 2]
        polymer = new_polymer

    counts = Counter(polymer)
    return counts.most_common(1)[0][1] - counts.most_common()[-1][1]


if __name__ == '__main__':
    with open('input.txt') as file:
        values = {}
        template = file.readline().strip()
        file.readline()
        rules = {}
        for line in file:
            pair, insertion = line.strip().split(' -> ')
            rules[pair] = insertion

    print(well_extend_my_polymer(template, rules, 10))
