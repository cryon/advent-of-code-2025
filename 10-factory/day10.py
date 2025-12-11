import re
import z3
from util import lines
from collections import namedtuple, deque

MACHINE_PATTERN = ("\\[(?P<lights>.*?)\\]\\s*"
                   "(?P<buttons>(?:\\(\\d+(?:,\\d+)*\\)\\s*)+)\\"
                   "{(?P<joltage>.*?)\\}")

Machine = namedtuple("Machine", "lights length buttons joltage")

def button_config(indices, length):
    return int("".join("1" if i in indices else "0" for i in range(length)), 2)

machines = []
for line in lines("input.txt", strip=True):
    if match := re.match(MACHINE_PATTERN, line):
        lights = int(match.group("lights").replace('.', '0').replace('#', '1'), 2)
        length = len(match.group("lights"))
        buttons = tuple(set(map(int, g[1:-1].split(","))) for g in match.group("buttons").split())
        joltage = tuple(int(n) for n in match.group("joltage").split(","))
        machines.append(Machine(lights, length, buttons, joltage))

def start_machine(machine):
    buttons_values = [button_config(b, machine.length) for b in machine.buttons]
    queue, seen = deque([(0, 0)]), set()
    while queue:
        state, presses = queue.popleft()
        if state == machine.lights: return presses
        if state in seen: continue
        seen.add(state)
        queue.extend((state^button, presses + 1) for button in buttons_values)

def tune_joltage(machine):
    solver = z3.Optimize()
    presses_var = z3.Int("presses")
    button_vars = [z3.Int(f"button-{i}") for i in range(len(machine.buttons))]

    for idx, joltage in enumerate(machine.joltage):
        buttons_affect_joltage = [i for i, button_configuration in enumerate(machine.buttons)
                                    if idx in button_configuration]
        solver.add(joltage == sum(button_vars[i] for i in buttons_affect_joltage))

    solver.add(button_var >= 0 for button_var in button_vars)
    solver.add(presses_var == sum(button_vars))

    solver.minimize(presses_var)
    solver.check()
    return int(str(solver.model()[presses_var]))

p1 = sum(start_machine(machine) for machine in machines)
p2 = sum(tune_joltage(machine) for machine in machines)

print(f"part1: {p1}, part2: {p2}")


