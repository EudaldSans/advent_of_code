from itertools import combinations_with_replacement
from typing import List
from tqdm import tqdm

from z3 import *


def find_led_combination(leds: List[str], buttons: List[List[int]]) -> int:
    r = 1
    while True:
        button_combos = combinations_with_replacement(buttons, r)

        for button_combo in button_combos:
            led_status = ['.'] * len(leds)
            for button_wiring in button_combo:
                for button in button_wiring:
                    led_status[button] = '#' if led_status[button] == '.' else '.'

            if led_status == leds:
                return r

        r += 1


def find_joltage_combination(joltages: List[int], buttons: List[List[int]]) -> int:
    vars = [Int(f"a{n}") for n in range(len(buttons))]

    solver = Solver()

    for b in vars:
        solver.add(b >= 0)

    for joltage_id, joltage in enumerate(joltages):
        expr = [vars[button_id] for button_id, button_wiring in enumerate(buttons) if joltage_id in button_wiring]
        solver.add(Sum(expr) == joltage)

    if solver.check() != sat:
        raise ValueError("Unsatisfiable solution")

    while solver.check() == sat:
        model = solver.model()
        n = sum([model[d].as_long() for d in model])
        solver.add(Sum(vars) < n)

    return n


def main():
    with open('diagram.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    led_result = 0
    joltage_result = 0
    for line in tqdm(lines, desc='Finding permutations'):
        fragments = line.split(' ')
        leds = list(fragments[0][1:-1])
        buttons = [list(map(int, button_wiring[1:-1].split(','))) for button_wiring in fragments[1:-1]]
        joltages = list(map(int, fragments[-1][1:-1].split(',')))

        led_result += find_led_combination(leds, buttons)
        joltage_result += find_joltage_combination(joltages, buttons)

    print(f'The sum of permutations for the LEDs is {led_result}')
    print(f'The sum of permutations for the joltages is {joltage_result}')


if __name__ == '__main__':
    main()
