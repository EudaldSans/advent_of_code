from computer import IntCodeComputer


if __name__ == '__main__':
    with open('program.tx') as file:
        text = file.readline()
        opcodes = [int(n) for n in text.split(',')]

    computer = IntCodeComputer(opcodes)
    index, result = computer.run_instance(12, 2)

    print(f'Exit program at {index}')
    print(f'Result = {result}')
