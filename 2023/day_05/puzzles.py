from typing import Tuple, List


class Seed:
    def __init__(self, start: int, length: int) -> None:
        self.start_location = start
        self.ranges = [(start, start + length)]

    def __repr__(self):
        return f"{self.start_location}->{self.ranges}"

    def get_closest_location(self) -> int:
        range_starts = [range_start for range_start, _ in self.ranges]
        return min(range_starts)


class SeedConverter:
    def __init__(self, name: str, map_lines: List[str]) -> None:
        self.name = name

        self.conversion_maps = [[int(x) for x in line.split()] for line in map_lines]

    def __repr__(self):
        return f"{self.name} map:\n{self.conversion_maps}"

    def convert_seed(self, seed: Seed) -> None:
        updated_ranges = list()
        for dst, src, size in self.conversion_maps:
            src_end = src + size

            new_seed_ranges = list()
            while seed.ranges:
                seed_start, seed_end = seed.ranges.pop()

                before_converter = (seed_start, min(seed_end, src))
                in_converter = (max(seed_start, src), min(src_end, seed_end))
                after_converter = (max(src_end, seed_start), seed_end)

                if before_converter[0] < before_converter[1]:
                    new_seed_ranges.append(before_converter)

                if in_converter[0] < in_converter[1]:
                    updated_ranges.append((in_converter[0] - src + dst, in_converter[1] - src + dst))

                if after_converter[0] < after_converter[1]:
                    new_seed_ranges.append(after_converter)

            seed.ranges = new_seed_ranges

        seed.ranges = seed.ranges + updated_ranges


def main(file_name: str) -> None:
    with open(file_name) as garden_file:
        garden_lines = garden_file.read()

    garden_parts = garden_lines.split('\n\n')
    seeds = garden_parts[0].split(':')[1].split(' ')[1:]
    seeds = [int(seed) for seed in seeds]
    garden_parts = garden_parts[1:]

    converters = list()
    for converter in garden_parts:
        converter_parts = converter.split('\n')
        converter_name = converter_parts[0].split(' ')[0]
        converter_lines = converter_parts[1:]
        converters.append(SeedConverter(converter_name, converter_lines))

    simple_seeds = [Seed(seed_value, 1) for seed_value in seeds]

    for seed in simple_seeds:
        for converter in converters:
            converter.convert_seed(seed)

    closest_location = min([seed.get_closest_location() for seed in simple_seeds])
    print(f'The closest location in the simple garden is {closest_location}')

    extended_seeds = [Seed(seed_start, seed_size) for seed_start, seed_size in zip(seeds[::2], seeds[1::2])]
    for seed in extended_seeds:
        for converter in converters:
            converter.convert_seed(seed)

    closest_location = min([seed.get_closest_location() for seed in extended_seeds])
    print(f'The closest location in the extended garden is {closest_location}')


if __name__ == '__main__':
    main('seed_map.txt')

