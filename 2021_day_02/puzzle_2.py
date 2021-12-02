

class Submarine:
    def __init__(self):
        self.horizontal_pos = 0
        self.depth = 0
        self._aim = 0

    def move_up(self, distance: int) -> None:
        self._aim -= distance

    def move_down(self, distance: int) -> None:
        self._aim += distance

    def move_forwards(self, distance: int) -> None:
        self.horizontal_pos += distance
        self.depth += self._aim*distance


def main(course_path: str):
    with open(course_path) as path_file:
        path = path_file.read().split('\n')

    submarine = Submarine()

    for command in path:
        direction, distance = command.split(' ')

        if direction == 'up':
            submarine.move_up(int(distance))
        elif direction == 'down':
            submarine.move_down(int(distance))
        elif direction == 'forward':
            submarine.move_forwards(int(distance))
        else:
            print('Unknown command.')

    result = submarine.horizontal_pos*submarine.depth
    print(f'Submarine position: ({submarine.horizontal_pos}, {submarine.depth}). Result: {result}')


if __name__ == '__main__':
    main('course.txt')
