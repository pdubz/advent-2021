#! /bin/python3


class Display:
    def __init__(self, patterns, displays):
        self.displays = [''.join(sorted(display)) for display in displays]
        patterns = [''.join(sorted(pattern)) for pattern in patterns]
        patterns.sort(key=len)

        self.numbers = {
            0: '',
            1: patterns[0],
            2: '',
            3: '',
            4: patterns[2],
            5: '',
            6: '',
            7: patterns[1],
            8: patterns[9],
            9: '',
        }

        self.__fit_six_nine_nice_zero(patterns[6:9])

        self.segment_top_right = Display.__non_overlapped_characters(self.numbers[6], self.numbers[8])
        self.segment_bottom_left = Display.__non_overlapped_characters(self.numbers[9], self.numbers[8])

        self.__fit_two_three_five(patterns[3:6])

        self.translation = {self.numbers[key]: key for key in self.numbers}

    @staticmethod
    def __contains_all_characters(check_string, char_set):
        return False not in [char in check_string for char in char_set]

    @staticmethod
    def __non_overlapped_characters(first, second):
        return set(first) ^ set(second)

    def __fit_six_nine_nice_zero(self, possible_fits):
        for fit in possible_fits:
            if Display.__contains_all_characters(fit, self.numbers[4]):
                self.numbers[9] = fit
            elif Display.__contains_all_characters(fit, self.numbers[1]) and \
                    not Display.__contains_all_characters(fit, self.numbers[4]):
                self.numbers[0] = fit
            else:
                self.numbers[6] = fit

    def __fit_two_three_five(self, possible_fits):
        for fit in possible_fits:
            if Display.__contains_all_characters(fit, self.numbers[1]):
                self.numbers[3] = fit
            elif Display.__contains_all_characters(fit, self.segment_bottom_left):
                self.numbers[2] = fit
            else:
                self.numbers[5] = fit

    def get_value(self):
        return int(f'{self.translation[self.displays[0]]}{self.translation[self.displays[1]]}{self.translation[self.displays[2]]}{self.translation[self.displays[3]]}')

    def __repr__(self):
        return f'{self.translation[self.displays[0]]}{self.translation[self.displays[1]]}{self.translation[self.displays[2]]}{self.translation[self.displays[3]]}'


def fix_displays(inputs: list):
    displays = []
    for line in inputs:
        display = Display(line[0].split(), line[1].split())
        displays.append(display.get_value())

    return sum(displays)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip().split('|') for line in file]

    print(fix_displays(values))
