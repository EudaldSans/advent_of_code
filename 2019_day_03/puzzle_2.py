from cable import Cable, find_intersections


def main():
    with open('circuit.txt') as file:
        cable_1 = Cable(file.readline().rstrip())
        cable_2 = Cable(file.readline().rstrip())

    intersections = find_intersections(cable_1, cable_2)

    for intersection in intersections:
        pass


if __name__ == '__main__':
    main()
