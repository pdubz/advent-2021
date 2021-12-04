#! /bin/python3

def slide_sweep(depths: list) -> str:
    increases = 0
    if len(depths) > 3:
        previous_depth = sum(depths[:3])
        for i in range(1, len(depths)):
            if i < len(depths) - 2:
                if sum(depths[i:i+3]) > previous_depth:
                    increases = increases + 1
                previous_depth = sum(depths[i:i+3])

    return increases


if __name__ == '__main__':
    with open('input.txt') as file:
        depths = [int(line.strip()) for line in file]

    print(slide_sweep(depths))
