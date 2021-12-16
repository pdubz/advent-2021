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


def embiggen(grid):
    embiggener = {
        1: 2,
        2: 3,
        3: 4,
        4: 5,
        5: 6,
        6: 7,
        7: 8,
        8: 9,
        9: 1
    }
    embiggened_grid = [row.copy() for row in grid]
    for iteration in range(4):
        for y in range(len(grid)):
            for x in range(len(grid[0])):
                embiggened_grid[y].append(embiggener[embiggened_grid[y][x + len(grid) * iteration]])

    for iteration in range(4):
        for y in range(len(grid)):
            row = []
            for x in range(len(embiggened_grid[0])):
                row.append(embiggener[embiggened_grid[y + len(grid) * iteration][x]])
            embiggened_grid.append(row)

    return embiggened_grid


if __name__ == '__main__':
    with open('input.txt') as file:
        values = []
        for line in file:
            values.append([int(char) for char in line.strip()])

    print(pathfind(embiggen(values)))
