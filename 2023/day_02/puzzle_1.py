from typing import Tuple
import re

red_filter = re.compile(r'(\d+) red')
green_filter = re.compile(r'(\d+) green')
blue_filter = re.compile(r'(\d+) blue')

_MAX_REDS = 12
_MAX_GREENS = 13
_MAX_BLUES = 14


def analyze_game(game_str: str) -> Tuple[bool, int]:
    game_id = int(game_str.split(':')[0].split(' ')[1])

    reds = [int(match) for match in red_filter.findall(game_str)]
    greens = [int(match) for match in green_filter.findall(game_str)]
    blues = [int(match) for match in blue_filter.findall(game_str)]

    if max(reds) > _MAX_REDS: return False, game_id
    if max(greens) > _MAX_GREENS: return False, game_id
    if max(blues) > _MAX_BLUES: return False, game_id

    return True, game_id


def main(file_name: str) -> int:
    with open(file_name, 'r') as game_file:
        game_lines = game_file.readlines()

    valid_id_sum = 0
    for line in game_lines:
        is_valid, game_id = analyze_game(line)
        if is_valid: valid_id_sum += game_id

    return valid_id_sum


if __name__ == '__main__':
    result = main('games.txt')
    print(f'Sum of valid game IDs: {result}')

