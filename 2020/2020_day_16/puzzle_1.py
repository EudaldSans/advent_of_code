import re
from collections import namedtuple
from typing import List

ticket_values_re = re.compile('[A-Za-z]+: ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
Range = namedtuple('Range', 'range_min range_max')


class RangeChecker:
    def __init__(self, ranges=List[Range]):
        self.ranges = ranges

    def __contains__(self, value: int) -> bool:
        for range in self.ranges:
            if range.range_min <= value <= range.range_max:
                return True

        return False


if __name__ == '__main__':
    with open('ticket_info.txt') as file:
        tickets = [line.rstrip() for line in file.readlines()]

    nearby_tickets = list()
    valid_ranges = list()
    for pos, line in enumerate(tickets):
        if 'nearby tickets' in line:
            nearby_tickets = tickets[pos+1:]
            break

        re_match = ticket_values_re.match(line)
        if re_match is not None:
            min1 = int(re_match.group(1))
            max1 = int(re_match.group(2))
            min2 = int(re_match.group(3))
            max2 = int(re_match.group(4))

            valid_ranges.append(Range(min1, max1))
            valid_ranges.append(Range(min2, max2))

    print(valid_ranges)
    checker = RangeChecker(valid_ranges)

    forbidden_values = list()
    for ticket in nearby_tickets:
        values = [int(value) for value in ticket.split(',')]

        for value in values:
            if value not in checker:
                forbidden_values.append(value)

    print(f'ticket scanning error rate: {sum(forbidden_values)}')


