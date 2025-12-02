import re
from collections import namedtuple
from typing import List

ticket_values_re = re.compile('([A-Za-z ]+): ([0-9]+)-([0-9]+) or ([0-9]+)-([0-9]+)')
Range = namedtuple('Range', 'range_min range_max')


class TicketField:
    UNASSIGNED_IDX = -1

    def __init__(self, range_1: Range, range_2: Range, name: str):
        self.name = name
        self.idx = TicketField.UNASSIGNED_IDX
        self.checker = RangeChecker([range_1, range_2])

        self.discarded_indexes = list()

    def __repr__(self):
        return f'{self.name}: {self.idx}'

    def check_value(self, value: int, index: int) -> bool:
        if value in self.checker:
            return True

        else:
            self.discarded_indexes.append(index)
            return False

    def is_index_discarded(self, index:int) -> bool:
        return index in self.discarded_indexes

    def assign_index(self, index: int):
        self.idx = index

    def is_assigned(self) -> bool:
        return self.idx != TicketField.UNASSIGNED_IDX


class Ticket:
    def __init__(self, ticket_values: List[int], fields: List[TicketField]):
        self.values = ticket_values
        self.fields = sorted(fields, key=lambda x: x.idx)

    def __repr__(self):
        output = list()
        for count, field in enumerate(self.fields):
            output.append(f'{field.name}: {self.values[count]}')

        return '\n'.join(output)

    def find_value(self, keyword: str) -> int:
        value = 1

        for field in self.fields:
            if keyword in field.name:
                value *= self.values[field.idx]

        return value


class RangeChecker:
    def __init__(self, ranges: List[Range]):
        self.ranges = ranges

    def __contains__(self, value: int) -> bool:
        for value_range in self.ranges:
            if value_range.range_min <= value <= value_range.range_max:
                return True

        return False


if __name__ == '__main__':
    with open('ticket_info.txt') as file:
        tickets = [line.rstrip() for line in file.readlines()]

    nearby_tickets = list()
    valid_ranges = list()
    ticket_fields: List[TicketField] = list()

    for pos, line in enumerate(tickets):
        if 'nearby tickets' in line:
            nearby_tickets = tickets[pos + 1:]
            break

        if 'your ticket:' in line:
            my_ticket = tickets[pos + 1]

        re_match = ticket_values_re.match(line)
        if re_match is not None:
            name = re_match.group(1)
            min1 = int(re_match.group(2))
            max1 = int(re_match.group(3))
            min2 = int(re_match.group(4))
            max2 = int(re_match.group(5))

            range_1 = Range(min1, max1)
            range_2 = Range(min2, max2)

            valid_ranges.append(range_1)
            valid_ranges.append(range_2)

            ticket_fields.append(TicketField(range_1, range_2, name))

    checker = RangeChecker(valid_ranges)

    print('Validating tickets')

    forbidden_values = list()
    valid_tickets = list()
    for ticket in nearby_tickets:
        values = [int(value) for value in ticket.split(',')]
        valid_ticket = True

        for value in values:
            if value not in checker:
                forbidden_values.append(value)
                valid_ticket = False

        if valid_ticket:
            valid_tickets.append(ticket)

    print(f'ticket scanning error rate: {sum(forbidden_values)}')
    print('Finding out ticket fields')

    valid_tickets.append(my_ticket)
    indexes_to_ignore = list()
    while len(indexes_to_ignore) != len(ticket_fields):
        for ticket in valid_tickets:
            values = [int(value) for value in ticket.split(',')]

            for index, value in enumerate(values):
                if index in indexes_to_ignore:
                    continue

                field_list = list()
                for field in ticket_fields:
                    if field.is_assigned() or field.is_index_discarded(index):
                        continue

                    if field.check_value(value, index):
                        field_list.append(field)

                if len(field_list) == 1:
                    field = field_list[0]
                    field.assign_index(index)
                    indexes_to_ignore.append(index)

                    print(f'Found out {field}')
                    break

    my_ticket = [int(value) for value in my_ticket.split(',')]
    my_ticket = Ticket(my_ticket, ticket_fields)

    print('My ticket is:')
    print(my_ticket)

    print(f'My departure result is: {my_ticket.find_value("departure")}')




