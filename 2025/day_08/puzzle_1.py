import math
from typing import List, Tuple, Optional


class JunctionBox():
    def __init__(self, x: int, y: int, z: int, id: int):
        self.x = x
        self.y = y
        self.z = z

        self.id = id
        self.connections = list()

    def __eq__(self, other: 'JunctionBox'):
        return self.id == other.id

    def __repr__(self):
        return f'JunctionBox {self.id} @ ({self.x}, {self.y}, {self.z})'

    def get_distance(self, other: 'JunctionBox') -> float:
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2 + (self.z - other.z)**2)

    def connect_to(self, other: 'JunctionBox'):
        self.connections.append(other)

    def is_connected(self, other: 'JunctionBox') -> bool:
        return other in self.connections

    def print_connections(self):
        print(f'{self} connects to:')
        for connection in self.connections:
            print(connection)

    def get_full_circuit(self, full_circuit: List['JunctionBox']) -> List['JunctionBox']:
        if self not in full_circuit:
            full_circuit.append(self)

        for connection in self.connections:
            if connection not in full_circuit:
                full_circuit.append(connection)
                full_circuit = connection.get_full_circuit(full_circuit)

        return full_circuit


def connect_next_closest_junction(junctions: List[JunctionBox], max_distance: float) -> Optional[Tuple[JunctionBox, JunctionBox]]:
    min_distance = max_distance
    closest_pair = None

    for junction_a in junctions:
        for junction_b in junctions:
            if junction_a == junction_b:
                continue

            distance = junction_a.get_distance(junction_b)
            if distance < min_distance and not junction_a.is_connected(junction_b):
                min_distance = distance
                closest_pair = (junction_a, junction_b)

    if closest_pair is not None:
        junction_a, junction_b = closest_pair

        junction_a.connect_to(junction_b)
        junction_b.connect_to(junction_a)

        return junction_a, junction_b

    else:
        return None


def part_1(junctions: List[JunctionBox], max_distance: float):
    required_connections = 1000
    performed_connections = 0
    while performed_connections < required_connections:
        if connect_next_closest_junction(junctions, max_distance) is not None:
            performed_connections += 1

    circuits = list()
    while len(junctions) > 0:
        circuit = list()
        circuit = junctions[0].get_full_circuit(circuit)

        for junction in circuit:
            junctions.remove(junction)

        circuits.append(circuit)

    second_circuit = list()
    third_circuit = list()
    first_circuit = list()
    for circuit in circuits:
        if len(circuit) > len(first_circuit):
            third_circuit = second_circuit
            second_circuit = first_circuit
            first_circuit = circuit

        elif len(circuit) > len(second_circuit):
            third_circuit = second_circuit
            second_circuit = circuit

        elif len(circuit) > len(third_circuit):
            third_circuit = circuit

    print(first_circuit)
    print(second_circuit)
    print(third_circuit)
    print(f'Result is: {len(first_circuit) * len(second_circuit) * len(third_circuit)}')


def main():
    with open('junction_boxes.txt', 'r') as f:
        lines = [line.rstrip('\n') for line in f.readlines()]

    id = 0
    junctions = list()
    for line in lines:
        x, y, z = line.split(',')

        junctions.append(JunctionBox(int(x), int(y), int(z), id))
        id += 1

    max_distance = 0
    for junction_a in junctions:
        for junction_b in junctions:
            if junction_a == junction_b:
                continue

            distance = junction_a.get_distance(junction_b)
            if distance > max_distance:
                max_distance = distance

    part_1(junctions, max_distance)


if __name__ == '__main__':
    main()
