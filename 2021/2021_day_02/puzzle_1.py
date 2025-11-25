

class Submarine:
    def __init__(self):
        self.horizontal_pos = 0
        self.depth = 0

    def move_up(self, distance: int) -> None:
        self.depth -= distance

    def move_down(self, distance: int) -> None:
        self.depth += distance

    def move_forwards(self, distance: int) -> None:
        self.horizontal_pos += distance


def main(course_path: str):
    with open(course_path) as path_file:
        path = path_file.read().split('\n')
        print(path)

    submarine = Submarine()

    for command in path:
        direction, distance = command.split(' ')

        match direction:
            case 'up':
                submarine.move_up(int(distance))
            case 'down':
                submarine.move_down(int(distance))
            case 'forward':
                submarine.move_forwards(int(distance))
            case _:
                raise TypeError('Unrecognised direction')

    result = submarine.horizontal_pos*submarine.depth
    print(f'Submarine position: ({submarine.horizontal_pos}, {submarine.depth}). Result: {result}')


if __name__ == '__main__':
    main('course.txt')

