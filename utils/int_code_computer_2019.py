from typing import List, Tuple


class IntCodeComputer:
    def __init__(self, opcodes: List[int]):
        self.opcodes = opcodes
        self.instruction_pointer = 0
        self.relative_base_pointer = 0
        self.outputs = list()

    def read_parameters(self, instruction: int, number_of_parameters: int, offset = 0) -> Tuple[int, ...]:
        parameters = list()

        for i in range(offset, number_of_parameters):
            parameter_position = -1
            instruction_type = (instruction // (10 ** (i + 2))) % 10

            match instruction_type:
                case 0: parameter_position = self.opcodes[self.instruction_pointer + 1 + i]
                case 1: parameter_position = self.instruction_pointer + 1 + i
                case 2: parameter_position = self.opcodes[self.instruction_pointer + 1 + i] + self.relative_base_pointer

            if parameter_position < 0:
                raise ValueError(f'{instruction} tried to read from negative memory at {parameter_position}')

            if parameter_position > len(self.opcodes):
                self.opcodes.extend([0] * (parameter_position - len(self.opcodes) + 4))

            parameters.append(self.opcodes[parameter_position])

        return tuple(parameters)

    def write_parameters(self, instruction: int, parameters: List[int], offset=0) -> None:
        for i, parameter in enumerate(parameters, start=offset):
            parameter_position = -1
            instruction_type = (instruction // (10 ** (i + 2))) % 10

            match instruction_type:
                case 0: parameter_position = self.opcodes[self.instruction_pointer + 1 + i]
                case 1: raise ValueError('Can not perform writes in immediate mode')
                case 2: parameter_position = self.opcodes[self.instruction_pointer + 1 + i] + self.relative_base_pointer

            if parameter_position < 0:
                raise ValueError(f'{instruction} tried to write to negative memory at {parameter_position}')

            if parameter_position > len(self.opcodes):
                self.opcodes.extend([0] * (parameter_position - len(self.opcodes) + 4))

            self.opcodes[parameter_position] = parameter

    def sum(self, instruction: int) -> None:
        a, b = self.read_parameters(instruction, 2)
        self.write_parameters(instruction, [a+b], offset=2)
        self.instruction_pointer += 4

    def product(self, instruction: int) -> None:
        a, b = self.read_parameters(instruction, 2)
        self.write_parameters(instruction, [a * b], offset=2)
        self.instruction_pointer += 4

    def input(self, instruction: int, program_input: int) -> None:
        self.write_parameters(instruction, [program_input])
        self.instruction_pointer += 2

    def output(self, instruction: int) -> None:
        value, = self.read_parameters(instruction, 1)
        self.outputs.append(value)
        self.instruction_pointer += 2

    def jump_if_true(self, instruction: int) -> None:
        a, b = self.read_parameters(instruction, 2)
        if a:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, instruction: int) -> None:
        a, b = self.read_parameters(instruction, 2)
        if a == 0:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    def less_than(self, instruction: int) -> None:
        a, b, pos = self.read_parameters(instruction, 3)
        if a < b:
            self.write_parameters(instruction, [1], offset=2)
        else:
            self.write_parameters(instruction, [0], offset=2)

        self.instruction_pointer += 4

    def equals(self, instruction: int) -> None:
        a, b = self.read_parameters(instruction, 2)

        if a == b:
            self.write_parameters(instruction, [1], offset=2)
        else:
            self.write_parameters(instruction, [0], offset=2)

        self.instruction_pointer += 4

    def adjust_relative_base(self, instruction: int) -> None:
        rel_pointer_mod, = self.read_parameters(instruction, 1)

        self.relative_base_pointer += rel_pointer_mod
        self.instruction_pointer += 2

    def run_instance(self, noun: int = None, verb: int = None, program_input: int = 0) -> Tuple[int, int]:
        if noun:
            self.opcodes[1] = noun
        if verb:
            self.opcodes[2] = verb

        while True:
            instruction = self.opcodes[self.instruction_pointer]
            op_code = instruction % 100

            match op_code:
                case 1: self.sum(instruction)
                case 2: self.product(instruction)
                case 3: self.input(instruction, program_input)
                case 4: self.output(instruction)
                case 5: self.jump_if_true(instruction)
                case 6: self.jump_if_false(instruction)
                case 7: self.less_than(instruction)
                case 8: self.equals(instruction)
                case 9: self.adjust_relative_base(instruction)
                case 99: return self.instruction_pointer, self.opcodes[0]
                case _: raise ValueError(f'Unrecognised instruction {instruction} at {self.instruction_pointer}')
