from typing import Tuple
import re

red_filter = re.compile(r'(\d+) red')
green_filter = re.compile(r'(\d+) green')
blue_filter = re.compile(r'(\d+) blue')

_MAX_REDS = 12
_MAX_GREENS = 13
_MAX_BLUES = 14


def analyze_game(game_str: str) -> int:
    reds = [int(match) for match in red_filter.findall(game_str)]
    greens = [int(match) for match in green_filter.findall(game_str)]
    blues = [int(match) for match in blue_filter.findall(game_str)]

    game_power = max(reds) * max(blues) * max(greens)

    return game_power


def main(file_name: str) -> int:
    with open(file_name, 'r') as game_file:
        game_lines = game_file.readlines()

    game_powers = [analyze_game(line) for line in game_lines]

    return sum(game_powers)


if __name__ == '__main__':
    result = main('games.txt')
    print(f'The sum of game powers is: {result}')
