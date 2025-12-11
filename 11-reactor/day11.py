import functools
from util import lines

devices = {s[0]:s[1].split() for l in lines("input.txt", strip=True) if (s:= l.split(":"))}

@functools.cache
def paths(current, goal, must_contain=frozenset()):
    if current == goal: return 0 if must_contain else 1
    return sum(paths(neighbour, goal, must_contain - {current}) for neighbour in devices[current])

p1 = paths("you", "out")
p2 = paths("svr", "out", frozenset(["dac", "fft"]))
print(f"part1: {p1}, part2: {p2}")