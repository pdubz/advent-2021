#! /bin/python3

class Binger:
    def __init__(self, board_strings):
        self.board = []
        for line in board_strings:
            self.board.append(line.split())

    def print_board(self):
        for line in self.board:
            print(line)

    def check_win(self):
        for line in self.board:
            if line.count('m') == 5:
                return True

        for i in range(5):
            if [char for char in self.board[i]].count('m') == 5:
                return True

        return False

    def remaining_sum(self):
        remaining = 0
        for line in self.board:
            remaining += sum([int(value) for value in line if value != 'm'])

        return remaining

    def play(self, number: str):
        for i in range(len(self.board)):
            if number in self.board[i]:
                self.board[i][self.board[i].index(number)] = 'm'


def bing_me(values: list, numbers: list):
    bings = []
    for i in range(1, len(values), 6):
        if values[i]:
            bing = Binger(values[i:i + 5])
            bings.append(bing)

    for number in numbers:
        for bing in bings:
            bing.play(number)
            if bing.check_win():
                return bing.remaining_sum() * int(number)


if __name__ == '__main__':
    with open('input.txt') as file:
        numbers = file.readline().split(',')

        values = [line.strip() for line in file]

    print(bing_me(values, numbers))
