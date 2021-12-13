#! /bin/python3

def find_paths(graph, node, path):
    results = []

    path = path + [node]
    if node == 'end':
        return [path]

    for next in graph[node]:
        if next != 'start':
            if next not in path or next.isupper():
                results.extend(find_paths(graph, next, path))

    return results


def path_me(inputs: dict):
    paths = find_paths(inputs, 'start', [])

    return len(paths)


if __name__ == '__main__':
    with open('input.txt') as file:
        values = {}
        for line in file:
            vertex1, vertex2 = line.strip().split('-')

            if vertex1 not in values:
                values[vertex1] = [vertex2]
            else:
                values[vertex1].append(vertex2)

            if vertex2 not in values:
                values[vertex2] = [vertex1]
            else:
                values[vertex2].append(vertex1)

    print(path_me(values))
