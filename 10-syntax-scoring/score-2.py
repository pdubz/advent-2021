#! /bin/python3

def parse(line):
    translators = {
        '(': ')',
        '[': ']',
        '{': '}',
        '<': '>'
    }
    expected = []
    for character in line:
        if character in translators.keys():
            expected.append(translators[character])
        elif character == expected[-1]:
            expected.pop()
        else:
            return 0

    score = 0
    scoring = {
        ')': 1,
        ']': 2,
        '}': 3,
        '>': 4
    }
    if len(expected) > 0:  # incomplete
        expected.reverse()
        for character in expected:
            score *= 5
            score += scoring[character]

    return score


def score_lines(inputs: list):
    scores = []
    for line in inputs:
        score = parse(line)
        if score > 0:
            scores.append(score)

    scores.sort()

    return scores[int(len(scores) / 2)]


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(score_lines(values))
