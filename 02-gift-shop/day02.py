from util import whole_file, chunker

def is_invalid(i, splits):
    return any(len(set(chunker(i, s))) == 1 for s in splits)

ranges = [range(int(p[0]), int(p[1]) + 1)
          for r in whole_file("input.txt").split(",")
          if (p := r.split("-"))]

p1 = sum(i for r in ranges for i in r if (s := str(i))
         and is_invalid(s, [len(s) // 2] if not len(s) % 2 else []))

p2 = sum(i for r in ranges for i in r if (s := str(i))
         and is_invalid(s, [f for f in range(1, len(s)) if not len(s) % f]))

print(f"part1: {p1}, part2: {p2}")



