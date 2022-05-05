from utils.int_code_computer_2019 import IntCodeComputer


class BreakIt(Exception):
    pass


if __name__ == '__main__':
    with open('program.tx') as file:
        text = file.readline()
        opcodes = [int(n) for n in text.split(',')]

    verb = -1
    noun = -1

    computer = IntCodeComputer(opcodes)

    try:
        for noun in range(100):
            for verb in range(100):
                index, result = computer.run_instance(noun, verb)

                if result == 19690720:
                    raise BreakIt

    except BreakIt:
        pass

    print(f'Verb: {verb}, noun:{noun}, Result = {100*noun + verb}')

