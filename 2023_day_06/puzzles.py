import numpy as np


def optimise_race(time: int, distance: int) -> int:
    wait_time = np.arange(time + 1)
    distance_travelled = (time - wait_time) * wait_time

    positive_outcomes = distance_travelled[distance_travelled > distance]

    return len(positive_outcomes)


def main(file_name: str) -> None:
    with open(file_name, 'r') as race_file:
        race_lines = race_file.readlines()

    distance_line = race_lines[1].strip('\n')
    distances = distance_line.split(' ')[1:]
    unkerned_distance = ''.join(distances)
    distances = [int(distance) for distance in distances if distance.isnumeric()]


    time_line = race_lines[0].strip('\n')
    times = time_line.split(' ')[1:]
    unkerned_time = ''.join(times)
    times = [int(time) for time in times if time.isnumeric()]

    races = zip(times, distances)

    error_margins = [optimise_race(time, distance) for time, distance in races]
    print(f'puzzle 1 margins: {error_margins}, result: {np.prod(error_margins)}')

    optimised_final_race = optimise_race(int(unkerned_time), int(unkerned_distance))
    print(f'puzzle 2 margins: {optimised_final_race}')


if __name__ == '__main__':
    main('races.txt')