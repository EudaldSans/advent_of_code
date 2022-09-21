
class Body:
    def __init__(self, orbit: str):
        self.parent, self.name = orbit.split(')')

    def __str__(self):
        return f'Planetary body {self.name} orbits {self.parent}'


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
