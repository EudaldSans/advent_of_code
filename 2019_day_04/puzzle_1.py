from utils.int_code_computer_2019 import IntCodeComputer


if __name__ == '__main__':
    with open('instructions.txt') as file:
        text = file.readline()
        opcodes = [int(n) for n in text.split(',')]

    computer = IntCodeComputer(opcodes)

    index, result = computer.run_instance(program_input=1)
    print(computer.outputs)

    print(f'{result}, {index}')
