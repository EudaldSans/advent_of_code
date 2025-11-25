from puzzle_1 import get_map_elements, navigate_map
import math


class Position:
    def __init__(self, starting_position):
        self.starting_position = starting_position
        self.current_position = starting_position

    def __repr__(self):
        return f'{self.starting_position}->{self.current_position}'


def main(map_file: str) -> int:
    indications, map_dict = get_map_elements(map_file)

    positions = [Position(position) for position in list(map_dict) if 'A' in position]

    steps_per_position = list()
    for position in positions:
        steps_per_position.append(navigate_map(indications, map_dict, starting_position=position.starting_position))

    return math.lcm(*steps_per_position)


if __name__ == '__main__':
    result = main('map.txt')

    print(f'It took {result} steps to reach the destination')

