def run_program(_instruction_pointer, _instructions, _accumulator, _executed_instructions):
    print('Testing new instruction')
    while True:
        if _instruction_pointer >= len(_instructions):
            print('Pointer out of bounds.')
            return True, _accumulator

        if _instruction_pointer in _executed_instructions:
            print('Program entered a loop!')
            return False, _accumulator

        _executed_instructions.append(_instruction_pointer)

        instruction, number = _instructions[_instruction_pointer].split(' ')

        if instruction == 'nop':
            _instruction_pointer += 1
            continue

        elif instruction == 'acc':
            _instruction_pointer += 1
            _accumulator += int(number)
            continue

        elif instruction == 'jmp':
            _instruction_pointer += int(number)
            continue

        else:
            print('Found unknown instruction!!')
            return False, _accumulator


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
            new_instruction_pointer = instruction_pointer + int(number)
            boot_successful, final_accumulator = run_program(new_instruction_pointer, instructions, accumulator, executed_instructions.copy())

            if boot_successful:
                accumulator = final_accumulator
                print(f'Change instruction {instruction_pointer} from nop to jmp')
                break

            instruction_pointer += 1
            continue

        elif instruction == 'acc':
            instruction_pointer += 1
            accumulator += int(number)
            continue

        elif instruction == 'jmp':
            new_instruction_pointer = instruction_pointer + 1
            boot_successful, final_accumulator = run_program(new_instruction_pointer, instructions, accumulator, executed_instructions.copy())

            if boot_successful:
                accumulator = final_accumulator
                print(f'Change instruction {instruction_pointer} from jmp to nop')
                break

            instruction_pointer += int(number)
            continue

        else:
            print('Found unknown instruction!!')
            break

    print(f'Final accumulator value {accumulator}')
