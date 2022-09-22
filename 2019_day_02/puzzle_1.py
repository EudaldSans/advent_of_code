from utils.int_code_computer_2019 import IntCodeComputer


if __name__ == '__main__':
    with open('program.txt') as file:
        text = file.readline()
        opcodes = [int(n) for n in text.split(',')]

    computer = IntCodeComputer(opcodes)
    index, result = computer.run_instance(12, 2)

    print(f'Exit program at {index}')
    print(f'Result = {result}')
