from typing import List

from copy import deepcopy

from tqdm import tqdm


class Range:
    def __init__(self, source, destination, length):
        self.source_start = source
        self.source_end = source + length - 1

        self.destination_start = destination
        self.destination_end = destination + length - 1

    def __contains__(self, item: int) -> bool:
        return self.source_start <= item <= self.source_end

    def convert(self, source: int) -> int:
        return self.destination_start + (source - self.source_start)


class ConversionMap:
    def __init__(self, map_lines: List[str], name: str) -> None:
        self.converter = dict()
        self.name = name
        self.ranges = list()

        for line in map_lines:
            destination, source, length = line.split(' ')
            self.ranges.append(Range(int(source), int(destination), int(length)))

    def __repr__(self):
        return f'{self.name} map with conversion values {self.converter}'

    def convert(self, source: int) -> int:
        for value_range in self.ranges:
            if source in value_range: return value_range.convert(source)

        return source


def main(file_name: str) -> None:
    with open(file_name, 'r') as file:
        map_lines = file.readlines()
        map_lines = [line.strip('\n') for line in map_lines]

    seeds = map_lines[0]
    seeds = seeds.split(' ')[1:]
    seeds = [int(seed) for seed in seeds]

    map_list = list()
    map_name = 'unknown'
    lines_start = 2
    map_lines = map_lines[2:]
    for count, line in tqdm(enumerate(map_lines), desc='Generating conversion maps'):
        if 'map' in line:
            map_name = (line.split(' '))[0]
            lines_start = count
        elif line == '':
            map_list.append(ConversionMap(map_lines[lines_start + 1: count], map_name))
            map_name = 'unknown'

    map_list.append(ConversionMap(map_lines[lines_start + 1: count], map_name))

    locations = list()
    for seed in seeds:
        location = seed
        for conversion_map in tqdm(map_list, desc=f'Converting seed {seed}'):
            location = conversion_map.convert(location)

        locations.append(location)

    closest_location = min(locations)
    closest_location_index = locations.index(closest_location)
    closest_seed = seeds[closest_location_index]

    '''for count, seed in enumerate(seeds):
        print(f'Seed number {seed} corresponds to soil number {locations[count]}')'''

    print(f'The closest location is {closest_location} for the seed {closest_seed}')

    paired_seeds = [(seeds[i - 1], seeds[i]) for i in range(len(seeds)) if i % 2 == 1]
    locations.clear()
    new_seeds = list()

    for seeds_start, seed_length in paired_seeds:
        print(range(seeds_start, seeds_start + seed_length, 1))
        for seed in tqdm(range(seeds_start, seeds_start + seed_length, 1), desc=f'Converting seed pair {seeds_start}, {seed_length}'):
            location = seed
            new_seeds.append(seed)
            for conversion_map in map_list:
                location = conversion_map.convert(location)

            locations.append(location)

    closest_location = min(locations)
    closest_location_index = locations.index(closest_location)
    closest_seed = new_seeds[closest_location_index]

    print(f'The closest location from the range is {closest_location} for the seed {closest_seed}')


if __name__ == '__main__':
    main('seed_map.txt')

