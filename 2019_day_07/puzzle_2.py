from itertools import permutations
import copy

from puzzle_1 import Amplifier, test_amplifiers

if __name__ == '__main__':
    with open('amplifier_sw.txt') as file:
        sequence = [int(code) for code in file.readline().split(',')]
        opcodes = [int(code) for code in file.readline().split(',')]

    sequence = [9, 8, 7, 6, 5]
    sequences = permutations(sequence)

    max_output = 0
    max_sequence = None

    amplifier_names = ['A', 'B', 'C', 'D', 'E']

    for count, sequence in enumerate(sequences):
        output = 0
        amplifiers = [Amplifier(copy.deepcopy(opcodes), f'{name}{count}') for name in amplifier_names]

        for amp_count, amplifier in enumerate(amplifiers[:-1]):
            amplifier.output_amp = amplifiers[amp_count + 1]

        amplifiers[-1].output_amp = amplifiers[0]

        output = test_amplifiers(amplifiers, sequence)
        if output > max_output:
            max_output = output
            max_sequence = sequence

    print(f'Maximum output {max_output}, achieved with sequence {max_sequence}')

