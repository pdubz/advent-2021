#! /bin/python3

def navigate(commands: list) -> str:
    x = 0
    y = 0

    if commands:
        for command in commands:
            if command[0] == "forward":
                x += int(command[1])
            elif command[0] == "down":
                y += int(command[1])
            elif command[0] == "up":
                y -= int(command[1])

    return str(x * y)


if __name__ == '__main__':
    with open('input.txt') as file:
        commands = [line.split(' ') for line in file]

    print(navigate(commands))
