#! /bin/python3

class Die:
    def __init__(self):
        self.roll_count = 0
        self.next_roll = 1

    def roll(self):
        self.roll_count += 1
        roll = self.next_roll
        self.next_roll = (self.next_roll + 1) % 100
        return roll


class Player:
    def __init__(self, id, pos):
        self.id = id
        self.position = pos - 1
        self.score = 0
        self.last_rolls = []
        self._pos_scorer = {
            0: 1,
            1: 2,
            2: 3,
            3: 4,
            4: 5,
            5: 6,
            6: 7,
            7: 8,
            8: 9,
            9: 10
        }

    def advance(self, rolls):
        for roll in rolls:
            print(f'Player {self.id} starts in pos {self.position + 1} and advances {roll} ', end='')
            self.position = ((self.position + roll) % 10)
            print(f'to position {self.position + 1}')
        self.score += self._pos_scorer[self.position]
        self.last_rolls = rolls


def rollin(p1_pos, p2_pos):
    die = Die()
    p1 = Player(1, p1_pos)
    p2 = Player(2, p2_pos)

    while p1.score < 1000 and p2.score < 1000:
        p1_rolls = []
        for i in range(3):
            p1_rolls.append(die.roll())

        p1.advance(p1_rolls)

        print(f'P1 rolls: {p1.last_rolls} P1 pos: {p1.position} P1 score: {p1.score}')

        if p1.score > 999:
            break

        p2_rolls = []
        for i in range(3):
            p2_rolls.append(die.roll())

        p2.advance(p2_rolls)

        print(f'P2 rolls: {p2.last_rolls} P2 pos: {p2.position} P2 score: {p2.score}')

    loser = min(p1.score, p2.score)
    print(f'Loser: {loser} RC: {die.roll_count}')
    return loser * die.roll_count


if __name__ == '__main__':
    with open('input.txt') as file:
        p1_start = int(file.readline().split()[-1])
        p2_start = int(file.readline().split()[-1])

    print(rollin(p1_start, p2_start))
