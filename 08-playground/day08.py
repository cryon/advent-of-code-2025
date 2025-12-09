from math import dist, prod
from itertools import combinations, islice
from util import lines

boxes = [tuple(int(num) for num in line.split(','))
         for line in lines("input.txt", strip=True)]

box_pairs = sorted([pair for pair in combinations(boxes, 2)],
                   key=lambda p: dist(*p))

def find_set(sets, key):
    return next((index for index, s in enumerate(sets) if key in s), -1)

def connect(limit=0):
    circuits = [{b} for b in boxes]
    for j1, j2 in (box_pairs[:limit] if limit else box_pairs):
        if (s1 := find_set(circuits, j1)) != (s2 := find_set(circuits, j2)):
            circuits.append(circuits[s1] | circuits[s2])
            circuits.pop(max(s1, s2))
            circuits.pop(min(s1, s2))
        if len(circuits) == 1: break
    return circuits, j1, j2

p1 = prod(len(l) for l in islice(sorted(connect(1000)[0], key=lambda x: len(x), reverse=True), 3))
_, j1, j2 = connect()

print(f"part1: {p1}, part2: {j1[0] * j2[0]}")