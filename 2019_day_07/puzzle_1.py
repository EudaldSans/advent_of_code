import copy
import time
from itertools import permutations
from typing import List, Tuple
from threading import Thread, Event, Lock

from utils.int_code_computer_2019 import IntCodeComputer


class Amplifier(IntCodeComputer):
    def __init__(self, opcodes: List[int], name: str):
        self.input_value = None
        self.input_event = Event()
        self.input_lock = Lock()
        self.output_amp = None
        self.name = name

        self.input_lock.acquire()

        super().__init__(opcodes)

    def enter_input(self, input: int):
        self.input_event.set()
        self.input_value = input
        self.input_lock.acquire()

    def input(self, instruction: int, program_input: int) -> None:
        self.input_event.wait(1)
        self.input_lock.release()
        if not self.input_event.is_set():
            raise ValueError(f'Input event of amp {self.name} timed out')

        self.input_event.clear()
        super().input(instruction, self.input_value)

    def output(self, instruction: int) -> None:
        super().output(instruction)
        output = self.outputs[-1]

        if self.output_amp is not None:
            self.output_amp.enter_input(output)

    def start(self):
        thread = Thread(target=super().run_instance)
        thread.start()


if __name__ == '__main__':
    with open('amplifier_sw.txt') as file:
        sequence = [int(code) for code in file.readline().split(',')]
        opcodes = [int(code) for code in file.readline().split(',')]

    sequences = permutations(sequence)

    max_output = 0
    max_sequence = None

    amplifier_names = ['A', 'B', 'C', 'D', 'E']

    for count, sequence in enumerate(sequences):
        output = 0
        amplifiers = [Amplifier(copy.deepcopy(opcodes), f'{name}{count}') for name in amplifier_names]

        for count, amplifier in enumerate(amplifiers[:-1]):
            amplifier.output_amp = amplifiers[count + 1]

        for amplifier, first_input in zip(amplifiers, sequence):
            amplifier.start()
            amplifier.enter_input(first_input)

        amplifiers[0].enter_input(0)

        while len(amplifiers[-1].outputs) == 0:
            time.sleep(5/1000)

        output = amplifiers[-1].outputs[0]

        if output > max_output:
            max_output = output
            max_sequence = sequence

    print(f'Maximum output {max_output}, achieved with sequence {max_sequence}')
