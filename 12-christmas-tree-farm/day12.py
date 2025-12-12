import re
from util import lines

REGION_PATTER = re.compile(r"^(\d+)x(\d+):\s(.*)$")

p1 = sum(a >= r for line in lines("input.txt")
         if (m := re.match(REGION_PATTER, line))     and
            (a := int(m.group(1)) * int(m.group(2))) and
            (r := sum(map(int, m.group(3).split())) * 9))

print(f"part1: {p1}, part2: :-)")
