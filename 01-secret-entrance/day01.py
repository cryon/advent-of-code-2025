from util import lines

def turn(current, clicks):
    return (current + clicks) % 100

turns = [int(l[1:]) * (1 if l[0] == 'R' else -1)
         for l in lines("input.txt", strip=True)]

a1, a2 = 50, 50
p1 = [a1 := turn(a1, t) for t in turns].count(0)
p2 = [a2 := turn(a2, click) for t in turns for click in ([-1] if t < 0 else [1]) * abs(t)].count(0)

print(f"part1: {p1}, part2: {p2}")

