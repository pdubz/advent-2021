#! /bin/python3

def sweep(depths: list) -> str:
    increases = 0
    if depths:
        previous_depth = depths[0]
        for depth in depths[1:]:
            if depth > previous_depth:
                increases += 1
            previous_depth = depth

    return increases


if __name__ == '__main__':
    with open('input.txt') as file:
        depths = [int(line.strip()) for line in file]

    print(sweep(depths))
