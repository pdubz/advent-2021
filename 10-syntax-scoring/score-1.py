#! /bin/python3

def parse(line):
    translator = '()[]{}<>'
    openers = ['(', '[', '{', '<']
    expected = []
    for character in line:
        if character in openers:
            expected.append(translator[translator.find(character) + 1])
        elif character == expected[-1]:
            expected.pop()
        else:
            if character == ')':
                return 3
            elif character == ']':
                return 57
            elif character == '}':
                return 1197
            elif character == '>':
                return 25137
            else:
                raise Exception('ruh roh')

    if len(expected) > 0:  # incomplete
        return 0
    return 0  # good


def score_lines(inputs: list):
    score = 0
    for line in inputs:
        score += parse(line)

    return score


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip() for line in file]

    print(score_lines(values))
