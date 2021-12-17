from pathlib import Path


def _parse_raw():
    this_dir = Path(__file__).parent
    inputs = this_dir.parent / "example.txt"
    raw = inputs.read_text()

    bits = bin(int(raw, 16))[2:].zfill(len(raw) * 4)

    return bits


BITS = _parse_raw()
print(BITS)
