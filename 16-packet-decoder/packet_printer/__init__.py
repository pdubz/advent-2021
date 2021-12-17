from pathlib import Path

import yaml

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

def _parse_raw():
    this_dir = Path(__file__).parent
    inputs = this_dir.parent / "input.txt"
    raw = inputs.read_text()

    bits = _bin_my_hex(raw)

    return bits


BITS = _parse_raw()
