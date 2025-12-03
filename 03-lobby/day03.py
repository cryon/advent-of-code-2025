from functools import reduce
from util import lines

def max_in_seq(s):
    return (idx := s.index(max(s))), s[idx]

def max_joltage(bank, n):
    idx, joltage = 0, []
    for i in range(n):
        idx_offset, v = max_in_seq(bank[idx:len(bank)-(n-i-1)])
        idx += idx_offset + 1
        joltage.append(v)
    return reduce(lambda x, y: x * 10 + y, joltage)

banks = [[int(b) for b in line] for line in lines("input.txt", strip=True)]

p1 = sum(max_joltage(bank, 2) for bank in banks)
p2 = sum(max_joltage(bank, 12) for bank in banks)

print(f"part1: {p1}, part2: {p2}")
