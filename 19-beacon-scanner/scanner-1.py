#! /bin/python3

import math


class Scanner:
    def __init__(self, id, beacons):
        self.id = id
        self.beacons = beacons

        self.signatures = []
        self._calculate_signatures()

        self.offset = [0, 0, 0]
        self.axis_map = [0, 1, 2]
        self.axis_sign = [1, 1, 1]

    def _calculate_signatures(self):
        for b1 in self.beacons:
            signatures = []
            for b2 in self.beacons:
                if b1 == b2:
                    continue
                signature = math.sqrt((b1[0] - b2[0]) ** 2 + (b1[1] - b2[1]) ** 2 + (b1[2] - b2[2]) ** 2)
                signatures.append(signature)
            signatures.sort()
            self.signatures.append(signatures)

    def find_overlap_and_align(self, other):
        common_beacons = {}
        for i, my_sig in enumerate(self.signatures):
            for j, other_sig in enumerate(other.signatures):
                count = 0
                if i in common_beacons:
                    break
                for k in range(12):
                    if my_sig[k] == other_sig[k]:
                        count += 1
                if count > 1:
                    common_beacons[i] = j

        if len(common_beacons) < 12:
            return False

        offset = [0, 0, 0]
        axis_map = [0, 1, 2]
        axis_sign = [1, 1, 1]

        for i in range(3):
            for j in [1, -1]:

                potential_x = []
                potential_y = []
                potential_z = []

                for key in common_beacons:
                    b1 = self.beacons[key]
                    b2 = other.beacons[common_beacons[key]]
                    potential_x.append(b1[0] - j * b2[i])
                    potential_y.append(b1[1] - j * b2[i])
                    potential_z.append(b1[2] - j * b2[i])

                if len(set(potential_x)) == 1:
                    axis_map[0] = i
                    axis_sign[0] = j
                    offset[0] = potential_x[0]
                if len(set(potential_y)) == 1:
                    axis_map[1] = i
                    axis_sign[1] = j
                    offset[1] = potential_y[0]
                if len(set(potential_z)) == 1:
                    axis_map[2] = i
                    axis_sign[2] = j
                    offset[2] = potential_z[0]

        other.offset = offset
        other.axis_map = axis_map
        other.axis_sign = axis_sign
        other.align_beacons()
        return True

    def align_beacons(self):
        for beacon in self.beacons:
            x, y, z = self.axis_map
            sign_x, sign_y, sign_z = self.axis_sign

            new_x = self.offset[0] + sign_x * beacon[x]
            new_y = self.offset[1] + sign_y * beacon[y]
            new_z = self.offset[2] + sign_z * beacon[z]

            beacon[0] = new_x
            beacon[1] = new_y
            beacon[2] = new_z


def scan(input):
    scanners = []
    for id, beacons in enumerate(input):
        scanners.append(Scanner(id, beacons))

    processed = [scanners[0]]
    processing = scanners[1:]

    while processing:
        current = processing.pop(0)
        for aligned in processed:
            is_aligned = aligned.find_overlap_and_align(current)
            if is_aligned:
                break

        if is_aligned:
            processed.append(current)
        else:
            processing.append(current)

    beacons = []
    for scanner in processed:
        for beacon in scanner.beacons:
            if beacon not in beacons:
                beacons.append(beacon)
                
    return len(beacons)


if __name__ == '__main__':
    values = []
    with open('input.txt') as file:
        scanner_beacons = []
        for line in file:
            if not line.strip():
                continue
            if line.startswith('---'):
                if len(scanner_beacons) > 0:
                    values.append(scanner_beacons)
                    scanner_beacons = []
                continue
            scanner_beacons.append([int(beacon) for beacon in line.strip().split(',')])

        values.append(scanner_beacons)

    print(scan(values))
