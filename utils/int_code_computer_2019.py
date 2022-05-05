from typing import List, Tuple


class IntCodeComputer:
    def __init__(self, opcodes: List[int]):
        self.opcodes = opcodes
        self.instruction_pointer = 0
        self.outputs = list()

    def obtain_parameters(self, instruction: int, number_of_parameters: int) -> Tuple[int, ...]:
        parameters = list()

        for i in range(number_of_parameters):
            parameter = self.opcodes[self.instruction_pointer + 1 + i]

            if instruction // 10**(i + 2) % 10 == 0:
                parameter = self.opcodes[parameter]

            parameters.append(parameter)

        return tuple(parameters)

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
                    a, b = self.obtain_parameters(instruction, 2)
                    pos = self.opcodes[self.instruction_pointer + 3]
                    self.opcodes[pos] = a + b
                    self.instruction_pointer += 4

                case 2:
                    a, b = self.obtain_parameters(instruction, 2)
                    pos = self.opcodes[self.instruction_pointer + 3]
                    self.opcodes[pos] = a * b
                    self.instruction_pointer += 4

                case 3:
                    pos = self.opcodes[self.instruction_pointer + 1]
                    self.opcodes[pos] = program_input
                    self.instruction_pointer += 2

                case 4:
                    pos, = self.obtain_parameters(instruction, 1)
                    self.outputs.append(pos)
                    self.instruction_pointer += 2

                case 5:
                    a, b = self.obtain_parameters(instruction, 2)
                    if a != 0:
                        self.instruction_pointer = b
                    else:
                        self.instruction_pointer += 3

                case 6:
                    a, b = self.obtain_parameters(instruction, 2)
                    if a == 0:
                        self.instruction_pointer = b
                    else:
                        self.instruction_pointer += 3

                case 7:
                    a, b = self.obtain_parameters(instruction, 2)
                    pos = self.opcodes[self.instruction_pointer + 3]

                    if a < b:
                        self.opcodes[pos] = 1
                    else:
                        self.opcodes[pos] = 0

                    self.instruction_pointer += 4

                case 8:
                    a, b = self.obtain_parameters(instruction, 2)
                    pos = self.opcodes[self.instruction_pointer + 3]

                    if a == b:
                        self.opcodes[pos] = 1
                    else:
                        self.opcodes[pos] = 0

                    self.instruction_pointer += 4

                case 99:
                    return self.instruction_pointer, self.opcodes[0]

                case _:
                    raise ValueError(f'Unrecognised instruction {instruction} at {self.instruction_pointer}')

        raise ValueError('Program ran without an exit instruction')

