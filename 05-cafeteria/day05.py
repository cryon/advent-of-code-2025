from itertools import takewhile
from util import lines

lines = lines("input.txt", strip=True)
ranges = [[int(s[0]), int(s[1]) + 1]
          for r in takewhile(lambda x: len(x), lines)
          if (s := r.split("-"))]
ingredients = [int(l) for l in lines]

def merge(intervals):
    intervals.sort(key=lambda interval: interval[0])
    merged = [intervals[0]]
    for start, end in intervals[1:]:
        prev_start, prev_end = merged[-1]
        if start <= prev_end:
            merged[-1][1] = max(prev_end, end)
        else:
            merged.append([start, end])
    return merged

merged = [range(*r) for r in merge(ranges)]
p1 = len([i for i in ingredients for r in merged if i in r])
p2 = sum(len(r) for r in merged)

print(f"part1: {p1}, part2: {p2}")
