from collections import Counter
from util import chars_with_coords, c_add

DIRS = [(0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1)]
rolls = {p for c, p in chars_with_coords("input.txt") if c == "@"}

def remove_rolls(r):
    access = Counter(c for d in DIRS for p in r if (c := c_add(p, d)) in r)
    return (res := {p for p, v in access.items() if v >= 4}), len(r) - len(res)

_, p1 = remove_rolls(rolls)

removed, p2 = 1, 0
while removed:
    rolls, removed = remove_rolls(rolls)
    p2 += removed

print(f"part1: {p1}, part2: {p2}")
