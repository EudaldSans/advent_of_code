from typing import List, Tuple


class IntCodeComputer:
    def __init__(self, opcodes: List[int]):
        self.opcodes = opcodes
        self.instruction_pointer = 0
        self.outputs = list()

    def obtain_parameters(self, instruction: int) -> Tuple[int, int, int]:
        param_1 = self.opcodes[self.instruction_pointer + 1]
        param_2 = self.opcodes[self.instruction_pointer + 2]
        param_3 = self.opcodes[self.instruction_pointer + 3]

        if instruction // 100 % 10 == 0:
            param_1 = self.opcodes[param_1]

        if instruction // 1000 % 10 == 0:
            param_2 = self.opcodes[param_2]

        return param_1, param_2, param_3

    def run_instance(self, noun: int = None, verb: int = None, program_input: int = 0) -> Tuple[int, int]:
        if noun:
            self.opcodes[1] = noun
        if verb:
            self.opcodes[2] = verb

        end_of_program = len(self.opcodes)

        while self.instruction_pointer < end_of_program:
            instruction = self.opcodes[self.instruction_pointer]
            op_code = instruction % 100

            match op_code:
                case 1:
                    a, b, pos = self.obtain_parameters(instruction)
                    self.opcodes[pos] = a + b
                    self.instruction_pointer += 4

                case 2:
                    a, b, pos = self.obtain_parameters(instruction)
                    self.opcodes[pos] = a * b
                    self.instruction_pointer += 4

                case 3:
                    pos = self.opcodes[self.instruction_pointer + 1]
                    self.opcodes[pos] = program_input
                    self.instruction_pointer += 2

                case 4:
                    pos = self.opcodes[self.instruction_pointer + 1]
                    self.outputs.append(self.opcodes[pos])
                    self.instruction_pointer += 2

                case 99:
                    return self.instruction_pointer, self.opcodes[0]

                case _:
                    raise ValueError(f'Unrecognised instruction {instruction} at {self.instruction_pointer}')

        raise ValueError('Program ran without an exit instruction')

