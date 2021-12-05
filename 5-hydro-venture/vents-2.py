#! /bin/python3

class Vent:
    def __init__(self, coords):
        pos1 = coords[0].split(',')
        pos2 = coords[1].split(',')
        self.x1 = int(pos1[0])
        self.y1 = int(pos1[1])
        self.x2 = int(pos2[0])
        self.y2 = int(pos2[1])

    def is_diagonal(self):
        return self.x1 != self.x2 and self.y1 != self.y2

    def __repr__(self):
        return f'{self.x1}.{self.y1} -> {self.x2}.{self.y2}'

    def max_x(self):
        return max(self.x1, self.x2)

    def max_y(self):
        return max(self.y1, self.y2)

    def direction(self):
        x_direction = 0
        if self.x1 - self.x2 > 0:
            x_direction = -1
        elif self.x1 - self.x2 < 0:
            x_direction = 1

        y_direction = 0
        if self.y1 - self.y2 > 0:
            y_direction = -1
        elif self.y1 - self.y2 < 0:
            y_direction = 1

        return x_direction, y_direction

    def magnitude(self):
        return max(abs(self.x1 - self.x2), abs(self.y1 - self.y2)) + 1


class VentMap:
    def __init__(self, vents):
        self.max_x = 0
        self.max_y = 0
        for vent in vents:
            if vent.max_x() > self.max_x:
                self.max_x = vent.max_x()
            if vent.max_y() > self.max_y:
                self.max_y = vent.max_y()

        self.map = []
        for y in range(self.max_y + 1):
            self.map.append([0] * (self.max_x + 1))

        for vent in vents:
            self.add_vent(vent)

    def print_map(self):
        print('map')
        for y in range(len(self.map)):
            for x in range(len(self.map[y])):
                print(self.map[x][y], end='')
            print()

    def add_vent(self, vent):
        x_dir, y_dir = vent.direction()

        x_pos = vent.x1
        y_pos = vent.y1

        for i in range(0, vent.magnitude()):
            self.map[y_pos][x_pos] += 1
            x_pos += x_dir
            y_pos += y_dir

    def get_overlaps(self):
        overlaps = 0
        for line in self.map:
            for point in line:
                if point > 1:
                    overlaps += 1
        return overlaps


def check_vents(vents: list):
    vents = [Vent(vent) for vent in vents]
    map = VentMap(vents)

    return map.get_overlaps()


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.strip().split(' -> ') for line in file]

    print(check_vents(values))
