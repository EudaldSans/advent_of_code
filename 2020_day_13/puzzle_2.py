from prettytable import PrettyTable
import operator
import functools
from typing import List


def do_crt(remainders: List[int], modules: List[int]) -> int:
    N = functools.reduce(operator.mul, modules, 1)
    results = list()
    x_list = list()

    # Chinese Remainder Theorem
    for bi, ni in zip(remainders, modules):
        # Make sure Ni is int, otherwise, for large numbers, float rounding error starts to be relevant
        Ni: int = N // ni
        xi = 0

        # Find inverse in module bi
        for i in range(1, ni):
            if ((Ni % ni) * i) % ni == 1:
                xi = i
                x_list.append(xi)
                break

        if xi == 0:
            raise ValueError('Could not find inverse mod')
        else:
            results.append(Ni * bi * xi)
    results = list(map(int, results))
    result_sum = sum(results)
    result = result_sum % N
    return result


def main(timetable_path) -> None:
    with open(timetable_path) as f:
        lines = f.readlines()

        if 'example' not in timetable_path:
            lines.pop(0)

        bus_strings = lines[0].rstrip('\n').split(',')
        number_of_entries = len(bus_strings)

    bus_ids = [int(time) if time != 'x' else 'x' for time in bus_strings]

    # Need bus id to depart at (t + pos): t + pos % id == 0  ->  t % id == - pos  ->  t % id == id - pos
    bus_remainders = [bus_id - bus_pos for bus_pos, bus_id in enumerate(bus_ids) if bus_id != 'x']
    bus_ids = [bus_id for bus_id in bus_ids if bus_id != 'x']

    timestamp = do_crt(bus_remainders, bus_ids)

    table = PrettyTable()
    field_names = [f'bus {bus_id}' for bus_id in bus_ids]
    field_names.insert(0, 'Time')

    table.field_names = field_names

    print(f'Found result for {timetable_path} at timestamp {timestamp}')

    for time in range(timestamp, timestamp + number_of_entries):
        row = list()
        row.append(time)

        for bus_id in bus_ids:
            if time % bus_id == 0:
                row.append('D')
            else:
                row.append('.')

        table.add_row(row)

    print(table)


if __name__ == '__main__':
    test_crt = do_crt([3, 1, 6], [5, 7, 8])
    print(f'Test for CRT is {test_crt}')    # Correct result 78
    test_crt = do_crt([2, 3, 2], [3, 5, 7])
    print(f'Test for CRT is {test_crt}')    # Correct result 78

    main('example_timetable_0.txt')         # Correct result 1068781
    main('example_timetable_1.txt')         # Correct result 3417
    main('example_timetable_2.txt')         # Correct result 754018
    main('example_timetable_3.txt')         # Correct result 779210
    main('example_timetable_4.txt')         # Correct result 1261476
    main('example_timetable_5.txt')         # Correct result 1202161486

    main('bus_timetable.tx')


