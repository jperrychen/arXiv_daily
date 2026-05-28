from __future__ import annotations

import math
import struct
import zlib
from pathlib import Path


WIDTH = 1200
HEIGHT = 512


def chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def mix(a: tuple[int, int, int], b: tuple[int, int, int], t: float) -> tuple[int, int, int]:
    return tuple(int(a[i] * (1 - t) + b[i] * t) for i in range(3))


def inside_rotated_rect(x: int, y: int, cx: float, cy: float, w: float, h: float, angle: float) -> bool:
    ca = math.cos(angle)
    sa = math.sin(angle)
    dx = x - cx
    dy = y - cy
    rx = dx * ca + dy * sa
    ry = -dx * sa + dy * ca
    return abs(rx) <= w / 2 and abs(ry) <= h / 2


def pixel(x: int, y: int) -> tuple[int, int, int]:
    top = (245, 248, 250)
    bottom = (224, 233, 238)
    base = mix(top, bottom, y / (HEIGHT - 1))

    if 115 <= x <= 1085 and 115 <= y <= 397:
        base = mix(base, (255, 255, 255), 0.66)

    if inside_rotated_rect(x, y, 385, 256, 330, 128, -0.22):
        base = mix(base, (52, 108, 176), 0.88)
    if inside_rotated_rect(x, y, 591, 246, 390, 126, 0.12):
        base = mix(base, (40, 157, 130), 0.86)
    if inside_rotated_rect(x, y, 795, 269, 310, 112, -0.08):
        base = mix(base, (238, 180, 72), 0.86)

    for cx, cy, radius, color in [
        (340, 248, 34, (248, 250, 252)),
        (590, 246, 34, (248, 250, 252)),
        (834, 270, 30, (248, 250, 252)),
    ]:
        dist = math.hypot(x - cx, y - cy)
        if dist <= radius:
            base = mix(base, color, 0.95)
        elif dist <= radius + 3:
            base = mix(base, (26, 32, 44), 0.22)

    if 220 <= x <= 980 and 428 <= y <= 435:
        base = mix(base, (65, 75, 90), 0.5)
    return base


def write_png(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    rows = []
    for y in range(HEIGHT):
        row = bytearray([0])
        for x in range(WIDTH):
            row.extend(pixel(x, y))
        rows.append(bytes(row))

    raw = b"".join(rows)
    png = b"\x89PNG\r\n\x1a\n"
    png += chunk(b"IHDR", struct.pack(">IIBBBBB", WIDTH, HEIGHT, 8, 2, 0, 0, 0))
    png += chunk(b"IDAT", zlib.compress(raw, level=9))
    png += chunk(b"IEND", b"")
    path.write_bytes(png)


if __name__ == "__main__":
    write_png(Path("images/cover.png"))
