import re

memory_re = re.compile('mem\[([0-9]+)] = ([0-9]+)')


class Memory:
    def __init__(self):
        self._and_mask = 0
        self._or_mask = 0

        self.memory = dict()

    def write_new_register(self, position: int, value: int) -> None:
        new_value = value & self._and_mask
        new_value = new_value | self._or_mask

        self.memory[position] = new_value

    def update_mask(self, new_mask: str):
        mask = new_mask.rstrip().replace('mask = ', '')

        self._and_mask = int(mask.replace('X', '1'), 2)
        self._or_mask = int(mask.replace('X', '0'), 2)

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
