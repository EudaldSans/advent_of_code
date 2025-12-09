from typing import List, Dict


def print_rays(rays: Dict[int, int], length: int):
    char_list = list()
    for x in range(length):
        if x in rays.keys():
            char_list.append('|')
        else:
            char_list.append('.')

    print(''.join(char_list))


def add_ray(ray: int, ray_positions: Dict[int, int], timelines: int):
    if ray_positions.get(ray) is None:
        ray_positions[ray] = timelines
    else:
        ray_positions[ray] += timelines


def main():
    with open('manifold.txt', 'r') as f:
        lines = [line.rstrip() for line in f.readlines()]

    initial_x = lines.pop(0).index('S')

    ray_positions = {initial_x: 1}
    splits = 0

    for y, line in enumerate(lines):
        new_positions = dict()
        print_rays(ray_positions, len(lines[0]))
        for ray, timelines in ray_positions.items():
            if line[ray] == '^':
                ray_1 = ray - 1
                add_ray(ray_1, new_positions, timelines)

                ray_2 = ray + 1
                add_ray(ray_2, new_positions, timelines)

                splits += 1

            else:
                add_ray(ray, new_positions, timelines)

        ray_positions = new_positions

    print(f'The beams will split {splits} times')
    print(f'There are {sum(ray_positions.values())} timelines')


if __name__ == '__main__':
    main()