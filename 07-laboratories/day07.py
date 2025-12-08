from collections import defaultdict
from util import lines

manifold = [(col, c) for line in lines("input.txt", strip=True)
                     for col, c in enumerate(line)]

splits, beams = 0, defaultdict(int)
for col, c in manifold:
    if c == 'S':
        beams[col] = 1
    elif c == '^' and col in beams:
        splits += 1
        beams[col - 1] += beams[col]
        beams[col + 1] += beams[col]
        del beams[col]

print(f"part1: {splits}, part2: {sum(beams.values())}")

