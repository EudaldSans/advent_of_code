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

    def sum(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        pos = self.opcodes[self.instruction_pointer + 3]
        self.opcodes[pos] = a + b
        self.instruction_pointer += 4

    def product(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        pos = self.opcodes[self.instruction_pointer + 3]
        self.opcodes[pos] = a * b
        self.instruction_pointer += 4

    def input(self, instruction: int, program_input: int) -> None:
        pos = self.opcodes[self.instruction_pointer + 1]
        self.opcodes[pos] = program_input
        self.instruction_pointer += 2

    def output(self, instruction: int) -> None:
        pos, = self.obtain_parameters(instruction, 1)
        self.outputs.append(pos)
        self.instruction_pointer += 2

    def jump_if_true(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        if a:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    def jump_if_false(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        if a == 0:
            self.instruction_pointer = b
        else:
            self.instruction_pointer += 3

    def less_than(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        pos = self.opcodes[self.instruction_pointer + 3]

        if a < b:
            self.opcodes[pos] = 1
        else:
            self.opcodes[pos] = 0

        self.instruction_pointer += 4

    def equals(self, instruction: int) -> None:
        a, b = self.obtain_parameters(instruction, 2)
        pos = self.opcodes[self.instruction_pointer + 3]

        if a == b:
            self.opcodes[pos] = 1
        else:
            self.opcodes[pos] = 0

        self.instruction_pointer += 4

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
                case 1: self.sum(instruction)
                case 2: self.product(instruction)
                case 3: self.input(instruction, program_input)
                case 4: self.output(instruction)
                case 5: self.jump_if_true(instruction)
                case 6: self.jump_if_false(instruction)
                case 7: self.less_than(instruction)
                case 8: self.equals(instruction)
                case 99: return self.instruction_pointer, self.opcodes[0]
                case _: raise ValueError(f'Unrecognised instruction {instruction} at {self.instruction_pointer}')

        raise ValueError('Program ran without an exit instruction')
