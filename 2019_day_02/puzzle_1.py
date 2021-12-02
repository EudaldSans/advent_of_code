def get_operators(opcodes, index):
    pos_a = opcodes[index + 1]
    pos_b = opcodes[index + 2]
    pos_store = opcodes[index + 3]

    op_a = opcodes[pos_a]
    op_b = opcodes[pos_b]

    return op_a, op_b, pos_store

if __name__ == '__main__':
    opcodes = list()
    with open('program.tx') as file:
        text = file.readline()
        opcodes = [int(n) for n in text.split(',')]

    opcodes[1] = 12
    opcodes[2] = 2

    print(opcodes)
    steps = range(0, len(opcodes), 4)

    for index in steps:
        if opcodes[index] == 1:
            a, b, pos = get_operators(opcodes, index)
            opcodes[pos] = a + b

        elif opcodes[index] == 2:
            a, b, pos = get_operators(opcodes, index)
            opcodes[pos] = a*b

        elif opcodes[index] == 99:
            print(f'Exit program at {index}')
            break

        else:
            print('Somehting went wrong')

    print(f'Result = {opcodes[0]}')



