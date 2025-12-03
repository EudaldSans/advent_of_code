

def find_joltage(battery_bank: str, batteries_required: int) -> int:
    joltage_values = [int(char) for char in battery_bank]

    total_joltage = 0
    start_of_next_bank = 0
    bank_size = len(joltage_values)
    for position in range(batteries_required, 0, -1):
        current_end = bank_size - position + 1
        current_bank = joltage_values[start_of_next_bank: current_end]

        best_bank = max(current_bank)
        total_joltage += best_bank * (10 ** (position - 1))

        start_of_next_bank = start_of_next_bank + current_bank.index(best_bank) + 1

    return total_joltage


def main():
    with open('battery_banks.txt', 'r') as f:
        battery_banks = [line.rstrip('\n') for line in f.readlines()]

    print(f'The sum of nominal joltages is: {sum([find_joltage(bank, 2) for bank in battery_banks])}')
    print(f'The sum of override joltages is: {sum([find_joltage(bank, 12) for bank in battery_banks])}')


if __name__ == '__main__':
    main()
