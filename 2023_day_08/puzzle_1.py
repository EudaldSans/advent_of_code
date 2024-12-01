import re
from typing import Tuple, List, Dict


def get_map_elements(map_file: str) -> Tuple[str, Dict[str, List[str]]]:
    with open(map_file) as directions_file:
        directions = directions_file.readlines()

    indications = directions[0].strip('\n')
    desert_map = directions[2:]

    map_dict = dict()
    rgx = re.compile('[%s]' % '() \n')

    for position in desert_map:
        position_elements = rgx.sub('', position).split('=')
        current_position = position_elements[0]
        next_positions = position_elements[1].split(',')
        map_dict[current_position] = next_positions

    return indications, map_dict


def navigate_map(indications: str, map_dict: Dict[str, List[str]], starting_position: str = 'AAA') -> int:
    current_step = 0
    indications_length = len(indications)
    current_position = starting_position

    while 'Z' not in current_position:
        next_direction = indications[current_step % indications_length]
        if next_direction == 'L':
            current_position = map_dict[current_position][0]
        elif next_direction == 'R':
            current_position = map_dict[current_position][1]
        else:
            raise ValueError(f'Direction {next_direction} should be either L or R')

        current_step += 1

    return current_step


def main(map_file: str) -> int:
    indications, map_dict = get_map_elements(map_file)
    return navigate_map(indications, map_dict)


if __name__ == '__main__':
    result = main('map.txt')

    print(f'It took {result} steps to reach the destination')

