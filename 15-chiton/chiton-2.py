#! /bin/python3

from queue import PriorityQueue


def add_vertex(grid, vertices, visited, risk, x, y):
    height = len(grid)
    width = len(grid[0])
    if x < 0 or y < 0 or x > width - 1 or y > height - 1 or (x, y) in visited:
        return
    weight = grid[x][y]
    vertices.put((weight + risk, (x, y)))
    visited.add((x, y))


def pathfind(input: list):
    height = len(input)
    width = len(input[0])

    next_vertex = PriorityQueue()
    next_vertex.put((0, (0, 0)))

    visited = set([(0, 0)])

    while next_vertex:
        current_risk, (current_x, current_y) = next_vertex.get()
        if current_y == height - 1 and current_x == width - 1:
            return current_risk

        add_vertex(input, next_vertex, visited, current_risk, current_x + 1, current_y)
        add_vertex(input, next_vertex, visited, current_risk, current_x - 1, current_y)
        add_vertex(input, next_vertex, visited, current_risk, current_x, current_y + 1)
        add_vertex(input, next_vertex, visited, current_risk, current_x, current_y - 1)

    return 'yikes'


if __name__ == '__main__':
    with open('input.txt') as file:
        values = []
        for line in file:
            values.append([int(char) for char in line.strip()])

    print(pathfind(values))
