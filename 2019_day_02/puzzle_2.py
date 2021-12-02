def get_operators(opcodes, index):
    pos_a = opcodes[index + 1]
    pos_b = opcodes[index + 2]
    pos_store = opcodes[index + 3]

    op_a = opcodes[pos_a]
    op_b = opcodes[pos_b]

    return op_a, op_b, pos_store


class BreakIt(Exception):
    pass


if __name__ == '__main__':
    with open('program.tx') as file:
        text = file.readline()
        original_opcodes = [int(n) for n in text.split(',')]

    verb = -1
    noun = -1

    print(original_opcodes)
    steps = range(0, len(original_opcodes), 4)
    try:
        for noun in range(100):
            for verb in range(100):
                opcodes = original_opcodes.copy()
                opcodes[1] = noun
                opcodes[2] = verb

                for index in steps:
                    if opcodes[index] == 1:
                        a, b, pos = get_operators(opcodes, index)
                        opcodes[pos] = a + b

                    elif opcodes[index] == 2:
                        a, b, pos = get_operators(opcodes, index)
                        opcodes[pos] = a*b

                    elif opcodes[index] == 99:
                        print(f'Exit program at {index} with {opcodes[0]}')
                        break

                    else:
                        print(f'Something went wrong with a {noun} and b {verb}')
                        break

                if opcodes[0] == 19690720:
                    raise BreakIt

    except BreakIt:
        pass

    print(f'Verb: {verb}, noun:{noun}, Result = {100*noun + verb}')

