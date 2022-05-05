from utils.int_code_computer_2019 import IntCodeComputer

if __name__ == '__main__':
    opcodes = [1,1,1,4,99,5,6,0,99]

    computer = IntCodeComputer(opcodes)

    index, result = computer.run_instance(1, 1)

    print(f'{result}, {index}')
