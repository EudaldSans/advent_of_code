from utils.int_code_computer_2019 import IntCodeComputer


if __name__ == '__main__':
    with open('boost_program.txt') as file:
        boost_program = [int(value) for value in file.readline().rstrip('\n').split(',')]

    computer = IntCodeComputer(boost_program)
    computer.run_instance(program_input=1)

    print(computer.outputs)
