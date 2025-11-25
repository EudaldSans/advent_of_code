import itertools
import math
from typing import List
from tqdm import tqdm

from multiprocessing.dummy import Pool as ThreadPool


def perform_operation(operators: List[int], operands: List[int], expected_result: int) -> int:
    result = operands[0]
    for count, operator in enumerate(operators):
        if operator == '+':
            result = result + operands[count + 1]
        if operator == '*':
            result = result * operands[count + 1]
        if operator == '|':
            result = int(str(result) + str(operands[count + 1]))

        if result > expected_result:
            return 0

    return result


def digits(n):
    return int(math.log10(n)) + 1


def ends_with(number, end):
    return (number - end) % 10 ** digits(end) == 0


def is_tractable(test_value, numbers, check_concat=True):
    *head, n = numbers
    if not head:
        return n == test_value

    q, r = divmod(test_value, n)
    if r == 0 and is_tractable(q, head, check_concat):
        return True

    if check_concat and ends_with(test_value, n) and is_tractable(test_value // (10 ** digits(n)), head, check_concat):
        return True

    return is_tractable(test_value - n, head, check_concat)


def check_operation(operation: str, check_concat: bool) -> int:
    result, operands = operation.split(':')

    result = int(result)

    operands = operands[1:]
    operands = [int(operand) for operand in operands.split(' ')]

    if is_tractable(result, operands, check_concat):
        return result

    else:
        return 0


def main(operation_file: str):
    with open(operation_file, 'r') as f:
        operations = [line.rstrip('\n') for line in f.readlines()]

    total_calibration = 0

    for operation in tqdm(operations):
       total_calibration += check_operation(operation, False)

    print(f'The result of the first calibration is {total_calibration}')

    total_calibration = 0

    for operation in tqdm(operations):
        total_calibration += check_operation(operation, True)

    print(f'The result of the second calibration is {total_calibration}')


if __name__ == '__main__':
    main('calibrations.txt')
