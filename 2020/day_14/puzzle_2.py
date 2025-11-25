import re
import itertools
import copy


memory_re = re.compile('mem\[([0-9]+)] = ([0-9]+)')


class Memory:
    def __init__(self):
        self._x_mask = ''
        self._or_mask = 0
        self._and_mask = 0
        self._x_appearances = 0

        self.memory = dict()

    def write_new_register(self, position: int, value: int) -> None:
        position = position | self._or_mask
        position = position & self._and_mask
        addresses_to_write = list()

        combinations = list(itertools.product(['0', '1'], repeat=self._x_appearances))
        combinations = [list(combination) for combination in combinations]

        initial_mask = self._x_mask.replace('1', '0')
        for combination in combinations:
            new_mask = initial_mask
            for byte in combination:
                last_x_index = new_mask.find('X')
                new_mask = new_mask[:last_x_index] + byte + new_mask[last_x_index + 1:]

            address_mask = int(new_mask, 2) | position
            addresses_to_write.append(address_mask)

        for address in addresses_to_write:
            self.memory[address] = value

    def update_mask(self, new_mask: str):
        mask = new_mask.rstrip().replace('mask = ', '')

        self._or_mask = int(mask.replace('X', '0'), 2)
        and_mask = mask.replace('0', '1')
        self._and_mask = int(and_mask.replace('X', '0'), 2)
        self._x_mask = mask.replace('1', '0')

        self._x_appearances = self._x_mask.count('X')

    def result(self) -> int:
        return sum(self.memory.values())


def main(program_path: str) -> None:
    with open(program_path) as program_file:
        instructions = program_file.readlines()

    memory = Memory()

    for instruction in instructions:
        matches = memory_re.match(instruction)
        if matches:
            position = int(matches.group(1))
            value = int(matches.group(2))

            memory.write_new_register(position, value)

        else:
            memory.update_mask(instruction)

    print(f'Final memory statet {memory.result()}')


if __name__ == '__main__':
    main('initialization_program.txt')
