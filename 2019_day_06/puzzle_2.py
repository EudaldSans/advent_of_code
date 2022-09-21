from puzzle_1 import Body

if __name__ == '__main__':
    with open('orbits.txt') as file:
        bodies = [Body(line.rstrip('\n')) for line in file.readlines()]
        orbits = {body.name: body for body in bodies}

    me = orbits['YOU']
    santa = orbits['SAN']

    print(me)
    print(santa)

    transfers_to_santa = me.find_distance_to_body(santa, orbits)

    print(f'{transfers_to_santa} orbital transfers are required to reach Santa')
