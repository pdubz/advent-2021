#! /bin/python3

class BinaryBuffer:
    def __init__(self, hex):
        self.location = 0
        self.buffer = BinaryBuffer._bin_my_hex(hex)

    @staticmethod
    def _bin_my_hex(hex):
        binary_string = ""
        converter = {
            '0': '0000',
            '1': '0001',
            '2': '0010',
            '3': '0011',
            '4': '0100',
            '5': '0101',
            '6': '0110',
            '7': '0111',
            '8': '1000',
            '9': '1001',
            'A': '1010',
            'B': '1011',
            'C': '1100',
            'D': '1101',
            'E': '1110',
            'F': '1111'
        }
        for char in hex:
            binary_string += converter[char]

        return binary_string

    def read(self, bits):
        if self.location >= len(self.buffer):
            return 'nope'
        read_bits = self.buffer[self.location:self.location + bits]
        self.location += bits
        return int(read_bits, 2)

    def read_str(self, bits):
        if self.location >= len(self.buffer):
            return 'nope'
        read_bits = self.buffer[self.location:self.location + bits]
        self.location += bits
        return read_bits

    def peek(self):
        return self.buffer[self.location:]


class BitsDecoder:
    def __init__(self, buffer: BinaryBuffer):
        self.version_sum = 0
        self.buffer = buffer
        self._evaluate_packet()

    def _evaluate_packet(self):
        version = self.buffer.read(3)
        type = self.buffer.read(3)
        self.version_sum += version

        if type == 4:
            literal_value = ''
            while self.buffer.read(1):
                literal_value += self.buffer.read_str(4)
            literal_value += self.buffer.read_str(4)
            return int(literal_value, 2)
        else:
            subpackets = []
            operator_length_type = self.buffer.read(1)
            if operator_length_type == 1:
                packet_count = self.buffer.read(11)
                for iteration in range(packet_count):
                    subpackets.append(self._evaluate_packet())
            else:
                length = self.buffer.read(15)
                buffer_start = self.buffer.location
                while self.buffer.location < buffer_start + length:
                    subpackets.append(self._evaluate_packet())



def decode(input):
    decoder = BitsDecoder(BinaryBuffer(input))
    return decoder.version_sum


if __name__ == '__main__':
    with open('input.txt') as file:
        value = file.readline().strip()

    print(decode(value))
