import re

numerical_filter = re.compile('\d')
advanced_filter = re.compile(r'(?=(\d|one|two|three|four|five|six|seven|eight|nine))')

translator_dict = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6, 'seven': 7, 'eight': 8, 'nine': 9}


def find_calibration_value(calibration_string: str, pattern: re.Pattern[str]) -> int:
    matches = pattern.findall(calibration_string)

    if len(matches) == 0: raise ValueError(f'There is no digit in {calibration_string}')

    matches = [int(match) if match.isdigit() else translator_dict[match]
               for match in matches]

    tens = matches[0]
    units = matches[-1]

    return tens * 10 + units


def main(file_name: str, pattern: re.Pattern[str]) -> int:
    with open(file_name, 'r') as file:
        lines = file.readlines()

    calibration_values = [find_calibration_value(string, pattern) for string in lines]
    return sum(calibration_values)


if __name__ == '__main__':
    result = main('example_1.txt', numerical_filter)
    print(f'The calibration value for example 1 is: {result}')

    result = main('example_2.txt', advanced_filter)
    print(f'The calibration value for example 2 is: {result}')

    result = main('calibration_document.txt', numerical_filter)
    print(f'The calibration value for puzzle 1 is: {result}')

    result = main('calibration_document.txt', advanced_filter)
    print(f'The calibration value for puzzle 2 is: {result}')

