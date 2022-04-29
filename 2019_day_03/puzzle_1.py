from cable import Cable, Point, find_intersections


def main():
    with open('circuit.txt') as file:
        cable_1 = Cable(file.readline().rstrip())
        cable_2 = Cable(file.readline().rstrip())

    intersections = find_intersections(cable_1, cable_2)

    starting_point = cable_1.starting_point
    best_point = Point(cable_1.GRID_SIZE, cable_1.GRID_SIZE)

    for intersection in intersections:
        if intersection == starting_point:
            continue

        if Cable.manhattan_distance(intersection) < Cable.manhattan_distance(best_point):
            best_point = intersection

    print(f'The final manhattan distance is: {Cable.manhattan_distance(best_point)}')


if __name__ == '__main__':
    main()
