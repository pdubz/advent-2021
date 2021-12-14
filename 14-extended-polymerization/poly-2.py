#! /bin/python3

def well_extend_my_polymer(polymer: str, rules: dict, iterations: int):
    combos = {key: 0 for key in rules.keys()}
    scores = {value: 0 for value in set(rules.values())}

    for location in range(len(polymer)):
        if location < len(polymer) - 1:
            combos[polymer[location:location + 2]] += 1
        scores[polymer[location]] += 1

    for iteration in range(iterations):
        new_combos = {key: 0 for key in rules.keys()}
        for combo, count in combos.items():
            insertion = rules[combo]
            new_combos[combo[0] + insertion] += count
            new_combos[insertion + combo[1]] += count
            scores[insertion] += count
        combos = new_combos

    return max(scores.values()) - min(scores.values())


if __name__ == '__main__':
    with open('input.txt') as file:
        values = {}
        template = file.readline().strip()
        file.readline()
        rules = {}
        for line in file:
            pair, insertion = line.strip().split(' -> ')
            rules[pair] = insertion

    print(well_extend_my_polymer(template, rules, 40))
