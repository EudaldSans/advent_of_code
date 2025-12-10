from itertools import combinations_with_replacement
from typing import List
from tqdm import tqdm


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
    r = min(joltages)
    while True:
        button_combos = combinations_with_replacement(buttons, r)
        for button_combo in button_combos:
            joltage_status = [0] * len(joltages)
            for button_wiring in button_combo:
                for button in button_wiring:
                    joltage_status[button] += 1

            if joltage_status == joltages:
                return r

        r += 1


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
        # joltage_result += find_joltage_combination(joltages, buttons)


    print(f'The sum of permutations for the LEDs is {led_result}')
    print(f'The sum of permutations for the jolrages is {joltage_result}')


if __name__ == '__main__':
    main()
