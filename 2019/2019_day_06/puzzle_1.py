from typing import Dict


class Body:
    def __init__(self, orbit: str):
        self.parent, self.name = orbit.split(')')

    def __str__(self):
        return f'Planetary body {self.name} orbits {self.parent}'

    def find_distance_to_body(self, body: 'Body', orbits: Dict[str, 'Body']) -> int:
        path_from_body_to_com = list()

        while body.parent != 'COM':
            path_from_body_to_com.append(body.name)
            body = orbits[body.parent]

        body = self
        distance_to_body = 0

        while body.parent not in path_from_body_to_com:
            distance_to_body += 1
            body = orbits[body.parent]

        intersection_index = path_from_body_to_com.index(body.parent)

        distance_to_body += intersection_index - 1  # Minus 1 because we don't want to orbit the object itself
        return distance_to_body


if __name__ == '__main__':
    with open('orbits.txt') as file:
        bodies = [Body(line.rstrip('\n')) for line in file.readlines()]
        orbits = {body.name: body for body in bodies}

    number_of_orbits = 0
    for body in orbits.values():
        while True:
            number_of_orbits += 1

            if body.parent == 'COM':
                break

            body = orbits[body.parent]

    print(f'There are {number_of_orbits} orbits in this system')
