from cable import Cable, find_intersections


def main():
    with open('circuit.txt') as file:
        cable_1 = Cable(file.readline().rstrip())
        cable_2 = Cable(file.readline().rstrip())

    intersections = find_intersections(cable_1, cable_2)

    min_steps = 0

    for intersection in intersections:
        if intersection == cable_2.starting_point:
            continue

        steps_1 = cable_1.steps_to_point(intersection)
        steps_2 = cable_2.steps_to_point(intersection)

        if steps_1 + steps_2 < min_steps:
            min_steps = steps_1 + steps_2

        if min_steps == 0:
            min_steps = steps_1 + steps_2

    print(f'The best steps for the cables are: {min_steps}')


if __name__ == '__main__':
    main()
