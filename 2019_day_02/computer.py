from typing import List, Tuple


class IntCodeComputer:
    def __init__(self, opcodes: List[int]):
        self.opcodes = opcodes

    def run_instance(self, noun: int, verb: int) -> Tuple[int, int]:
        opcodes = self.opcodes.copy()
        opcodes[1] = noun
        opcodes[2] = verb

        for index in range(0, len(opcodes), 4):
            match opcodes[index]:
                case 1:
                    pos_a = opcodes[index + 1]
                    pos_b = opcodes[index + 2]

                    pos = opcodes[index + 3]
                    a = opcodes[pos_a]
                    b = opcodes[pos_b]

                    opcodes[pos] = a + b

                case 2:
                    pos_a = opcodes[index + 1]
                    pos_b = opcodes[index + 2]

                    pos = opcodes[index + 3]
                    a = opcodes[pos_a]
                    b = opcodes[pos_b]

                    opcodes[pos] = a * b

                case 99:
                    return index, opcodes[0]

                case _:
                    raise ValueError(f'Unrecognised opcode {opcodes[index]} at {index}')

        raise ValueError('Program ran without an exit instruction')

