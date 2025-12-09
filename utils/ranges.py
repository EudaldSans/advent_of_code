from collections import namedtuple
from typing import List


Range = namedtuple('Range', 'min max')


def value_in_range_exclusive(value_range: Range, value: int) -> bool:
    return value_range.min < value < value_range.max


def value_in_range_inclusive(value_range: Range, value: int) -> bool:
    return value_range.min <= value <= value_range.max


class RangeChecker:
    def __init__(self, ranges: List[Range], check_function: callable):
        self.ranges = ranges
        self.check_function = check_function

    def __contains__(self, value: int) -> bool:
        for value_range in self.ranges:
            if self.check_function(value_range, value):
                return True

        return False


class InclusiveRangeChecker(RangeChecker):
    def __init__(self, ranges: List[Range]):
        super().__init__(ranges, value_in_range_inclusive)


class ExclusiveRangeChecker(RangeChecker):
    def __init__(self, ranges: List[Range]):
        super().__init__(ranges, value_in_range_exclusive)
