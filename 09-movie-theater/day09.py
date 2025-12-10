from collections import deque
from itertools import combinations
from util import lines, c_add

REDS = [tuple(map(int, line.split(","))) for line in lines("input.txt", strip=True)]
X_MAP = {x: i for i, x in enumerate(sorted(set(x for x, _ in REDS)))}
Y_MAP = {y: i for i, y in enumerate(sorted(set(y for _, y in REDS)))}
BOUNDS = (list(X_MAP.values())[-1], list(Y_MAP.values())[-1])

def pairwise_circle(lst):
    return [(lst[i - 1], lst[i]) for i in range(len(lst))]

def line(p1, p2):
    x_range = range(min(p1[0], p2[0]), max(p1[0], p2[0]) + 1)
    y_range = range(min(p1[1], p2[1]), max(p1[1], p2[1]) + 1)
    return [(x, p1[1]) for x in x_range] if p1[1] == p2[1] else [(p1[0], y) for y in y_range]

def area(p1, p2):
    return (abs(p1[0] - p2[0]) + 1) * (abs(p1[1] - p2[1]) + 1)

def compress(p):
    return X_MAP[p[0]], Y_MAP[p[1]]

def fill(vertices, bounds):
    filled = set()
    queue = deque([(-1, -1)])
    while queue:
        p = queue.popleft()
        if (not -1 <= p[0] <= bounds[0] + 1 or
            not -1 <= p[1] <= bounds[1] + 1 or
            p in filled or p in vertices):
            continue

        filled.add(p)
        queue.extend(c_add(p, d) for d in [(-1, 0), (1, 0), (0, -1), (0, 1)])
    return filled

def rectangle_perimeter(p1, p2):
    (x1, y1), (x2, y2) = p1, p2
    coords = set()

    for y in range(min(y1, y2), max(y1, y2) + 1):
        coords.add((min(x1, x2), y))
        coords.add((max(x1, x2), y))
    for x in range(min(x1, x2), max(x1, x2) + 1):
        coords.add((x, min(y1, y2)))
        coords.add((x, max(y1, y2)))

    return coords

polygon = {p for p1, p2 in pairwise_circle(REDS) for p in line(compress(p1), compress(p2))}
exterior = fill(polygon, BOUNDS)
areas = sorted([(area(p1, p2), p1, p2) for p1, p2 in combinations(REDS, 2)], reverse=True)

for a, p1, p2 in areas:
    perimeter = rectangle_perimeter(compress(p1), compress(p2))
    if all(c not in exterior for c in perimeter):
        break

print(f"part1: {areas[0][0]}, part2: {a}")
