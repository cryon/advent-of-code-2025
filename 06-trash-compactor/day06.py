import operator
from functools import reduce
from itertools import groupby
from util import lines

OPS = {'+': operator.add, '*': operator.mul}
full_input = [[c for c in row.rstrip('\n')] for row in lines("input.txt")]
rotated_input = [''.join(c).strip() for c in reversed([col for col in zip(*full_input[:-1])])]

operators = [OPS[o] for o in full_input[-1] if o != ' ']
numbers = zip(*[[int(n) for n in ''.join(r).split()] for r in full_input[:-1]])
cephalopod_numbers = reversed([[int(i) for i in g] for k, g in groupby(rotated_input, lambda x: x == '') if not k])

p1 = sum(reduce(op, next(numbers)) for op in operators)
p2 = sum(reduce(op, next(cephalopod_numbers)) for op in operators)

print(f"part1: {p1}, part2: {p2}")
