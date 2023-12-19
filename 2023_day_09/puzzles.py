from typing import List, Tuple

def find_value_history(value_sequence: List[int]) -> List[Tuple[int, int]]:
    history_found = False

    output_sequence = [(value_sequence[0], value_sequence[-1])]

    while not history_found:
        history_found = True
        new_sequence = list()
        for i in range(len(value_sequence) - 1):
            new_value = value_sequence[i + 1] - value_sequence[i]
            new_sequence.append(new_value)
            if new_value != 0: history_found = False

        output_sequence.append((new_sequence[0], new_sequence[-1]))
        value_sequence = new_sequence

    return output_sequence


def extrapolate_values(value_sequence: List[Tuple[int, int]]) -> Tuple[int, int]:
    value_sequence = value_sequence[::-1]

    future_value = 0
    past_value = 0
    for first_value, last_value in value_sequence:
        future_value += last_value
        past_value = first_value - past_value

    return past_value, future_value


def main(file_name: str) -> None:
    with open(file_name, 'r') as sequences_file:
        sequences = sequences_file.readlines()

    extrapolated_values = list()
    for sequence in sequences:
        sequence = sequence.strip('\n')
        sequence = [int(value) for value in sequence.split(' ')]

        sequence_history = find_value_history(sequence)

        extrapolated_values.append(extrapolate_values(sequence_history))

    future_values = [value for _, value in extrapolated_values]
    past_values = [value for value, _ in extrapolated_values]

    print(f'The sum of the future values is: {sum(future_values)}')
    print(f'The sum of the past values is: {sum(past_values)}')


if __name__ == "__main__":
    main('OASIS_output.txt')


