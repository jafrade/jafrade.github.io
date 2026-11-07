"""Make the tab and home-screen icons: the nav's half-disc mark.

    python3 tools/make-favicons.py

Draws the mark from the same geometry as favicon.svg and .mark .disc in
css/site.css (a 26-unit ink disc with an oak half-disc of radius 7), so no
browser or image tool is needed. Writes favicon.ico (16, 32 and 48px) and
apple-touch-icon.png (180px, the mark on paper with some margin).
"""
import struct
import zlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
INK, OAK, PAPER = (0x2A, 0x27, 0x24), (0xB8, 0x8B, 0x60), (0xF5, 0xF0, 0xE7)


def colour_at(x, y):
    """Colour of the mark at (x, y) in its 26-unit box, or None outside it."""
    if (x - 13) ** 2 + (y - 13) ** 2 > 13 ** 2:
        return None
    if x >= 13 and (x - 13) ** 2 + (y - 13) ** 2 <= 7 ** 2:
        return OAK
    return INK


def draw(size, mark=None, background=None, samples=8):
    """RGBA rows for a size × size image, with the mark filling `mark` pixels."""
    mark = mark or size
    pad = (size - mark) / 2
    rows = []
    for py in range(size):
        row = bytearray()
        for px in range(size):
            r = g = b = a = 0
            for sy in range(samples):
                for sx in range(samples):
                    x = (px + (sx + .5) / samples - pad) * 26 / mark
                    y = (py + (sy + .5) / samples - pad) * 26 / mark
                    c = colour_at(x, y) or background
                    if c:
                        r, g, b, a = r + c[0], g + c[1], b + c[2], a + 1
            n = samples * samples
            # Colours are averaged over covered samples; coverage sets alpha.
            row += bytes((r // a, g // a, b // a, round(255 * a / n))) if a else bytes(4)
        rows.append(bytes(row))
    return rows


def png(rows):
    size = len(rows)
    raw = b"".join(b"\0" + r for r in rows)

    def chunk(kind, data):
        return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data))
    return (b"\x89PNG\r\n\x1a\n" + chunk(b"IHDR", struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0))
            + chunk(b"IDAT", zlib.compress(raw, 9)) + chunk(b"IEND", b""))


sizes = (16, 32, 48)
images = [png(draw(s)) for s in sizes]
offset, entries = 6 + 16 * len(images), b""
for s, data in zip(sizes, images):
    entries += struct.pack("<BBBBHHII", s, s, 0, 0, 1, 32, len(data), offset)
    offset += len(data)
(ROOT / "favicon.ico").write_bytes(struct.pack("<HHH", 0, 1, len(images)) + entries + b"".join(images))
(ROOT / "apple-touch-icon.png").write_bytes(png(draw(180, mark=120, background=PAPER, samples=4)))
print("wrote favicon.ico and apple-touch-icon.png")
