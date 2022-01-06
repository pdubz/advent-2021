#! /bin/python3

# I'll just go ahead and leave this as a testament to the need for reading the whole problem before starting work, cause
# this was never going to be able to be used for serious calculations

class Alu:
    def __init__(self, inputs):
        self.w, self.x, self.y, self.z = 0, 0, 0, 0
        self.inputs = inputs

    def process(self, command, *expression):
        if command == 'inp' and len([*expression]) == 1:
            self.inp(*expression)
        elif command == 'add' and len([*expression]) == 2:
            self.add(*expression)
        elif command == 'mul' and len([*expression]) == 2:
            self.mul(*expression)
        elif command == 'div' and len([*expression]) == 2:
            self.div(*expression)
        elif command == 'mod' and len([*expression]) == 2:
            self.mod(*expression)
        elif command == 'eql' and len([*expression]) == 2:
            self.eql(*expression)
        else:
            print(f'Unable to process: {command} with target: {expression}')

    def inp(self, *expression):
        if len(self.inputs) < 1:
            print(f'inp called with no inputs left to process')
            return
        if expression[0] == 'w':
            self.w = self.inputs.pop(0)
        elif expression[0] == 'x':
            self.x = self.inputs.pop(0)
        elif expression[0] == 'y':
            self.y = self.inputs.pop(0)
        elif expression[0] == 'z':
            self.z = self.inputs.pop(0)
        else:
            print(f'Invalid target for input instruction: {expression}')

    def add(self, *expression):
        if expression[1].lstrip('-').isnumeric():
            value = int(expression[1])
        else:
            if expression[1] == 'w':
                value = self.w
            elif expression[1] == 'x':
                value = self.x
            elif expression[1] == 'y':
                value = self.y
            elif expression[1] == 'z':
                value = self.z
            else:
                print(f'Invalid second operand for add instruction: {expression}')
                return
        if expression[0] == 'w':
            self.w += value
        elif expression[0] == 'x':
            self.x += value
        elif expression[0] == 'y':
            self.y += value
        elif expression[0] == 'z':
            self.z += value
        else:
            print(f'Invalid first operand for add instruction: {expression}')

    def mul(self, *expression):
        if expression[1].lstrip('-').isnumeric():
            value = int(expression[1])
        else:
            if expression[1] == 'w':
                value = self.w
            elif expression[1] == 'x':
                value = self.x
            elif expression[1] == 'y':
                value = self.y
            elif expression[1] == 'z':
                value = self.z
            else:
                print(f'Invalid second operand for mul instruction: {expression}')
                return
        if expression[0] == 'w':
            self.w *= value
        elif expression[0] == 'x':
            self.x *= value
        elif expression[0] == 'y':
            self.y *= value
        elif expression[0] == 'z':
            self.z *= value
        else:
            print(f'Invalid first operand for mul instruction: {expression}')

    def div(self, *expression):
        if expression[1].lstrip('-').isnumeric():
            value = int(expression[1])
        else:
            if expression[1] == 'w':
                value = self.w
            elif expression[1] == 'x':
                value = self.x
            elif expression[1] == 'y':
                value = self.y
            elif expression[1] == 'z':
                value = self.z
            else:
                print(f'Invalid second operand for div instruction: {expression}')
                return
        if expression[0] == 'w':
            self.w //= value
        elif expression[0] == 'x':
            self.x //= value
        elif expression[0] == 'y':
            self.y //= value
        elif expression[0] == 'z':
            self.z //= value
        else:
            print(f'Invalid first operand for div instruction: {expression}')

    def mod(self, *expression):
        if expression[1].lstrip('-').isnumeric():
            value = int(expression[1])
        else:
            if expression[1] == 'w':
                value = self.w
            elif expression[1] == 'x':
                value = self.x
            elif expression[1] == 'y':
                value = self.y
            elif expression[1] == 'z':
                value = self.z
            else:
                print(f'Invalid second operand for div instruction: {expression}')
                return
        if expression[0] == 'w':
            self.w %= value
        elif expression[0] == 'x':
            self.x %= value
        elif expression[0] == 'y':
            self.y %= value
        elif expression[0] == 'z':
            self.z %= value
        else:
            print(f'Invalid first operand for div instruction: {expression}')

    def eql(self, *expression):
        if expression[1].lstrip('-').isnumeric():
            value = int(expression[1])
        else:
            if expression[1] == 'w':
                value = self.w
            elif expression[1] == 'x':
                value = self.x
            elif expression[1] == 'y':
                value = self.y
            elif expression[1] == 'z':
                value = self.z
            else:
                print(f'Invalid second operand for div instruction: {expression}')
                return
        if expression[0] == 'w':
            self.w = int(self.w == value)
        elif expression[0] == 'x':
            self.x = int(self.x == value)
        elif expression[0] == 'y':
            self.y = int(self.y == value)
        elif expression[0] == 'z':
            self.z = int(self.z == value)
        else:
            print(f'Invalid first operand for div instruction: {expression}')

    def __repr__(self):
        return f'w: {self.w}\nx: {self.x}\ny: {self.y}\nz: {self.z}'


def im_rubber_ur_alu(input):
    alu = Alu([1, 3, 5, 7, 9, 2, 4, 6, 8, 9, 9, 9, 9, 9])
    for command in input:
        alu.process(command[0], *command[1:])

    return alu


if __name__ == '__main__':
    with open('input.txt') as file:
        values = [line.split() for line in file]

    print(im_rubber_ur_alu(values))
