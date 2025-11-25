if __name__ == '__main__':
    with open('instructions.tx') as f:
        total_questions = 0
        instructions = list()
        for line in f:  # read rest of lines
            instructions.append(line.rstrip('\n'))

    program_done = False
    instruction_pointer = 0
    accumulator = 0
    executed_instructions = list()

    while not program_done:
        if instruction_pointer > len(instructions):
            print('Pointer out of bounds.')
            break

        if instruction_pointer in executed_instructions:
            print('Program entered a loop!')
            break

        executed_instructions.append(instruction_pointer)

        instruction, number = instructions[instruction_pointer].split(' ')

        if instruction == 'nop':
            instruction_pointer += 1
            continue

        elif instruction == 'acc':
            instruction_pointer += 1
            accumulator += int(number)
            continue

        elif instruction == 'jmp':
            instruction_pointer += int(number)
            continue

        else:
            print('Found unknown instruction!!')
            break

    print(f'Final accumulator value {accumulator}')
