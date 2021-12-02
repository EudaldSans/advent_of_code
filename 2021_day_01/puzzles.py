from typing import Tuple


class SlidingWindow:
    def __init__(self, iterable: list):
        self._iterable = iterable
        self._len = len(iterable)

    def go_through_window(self, step_size: int) -> Tuple[int, int]:
        for i in range(self._len - step_size):
            first_batch = sum(self._iterable[i: i + step_size])
            second_batch = sum(self._iterable[i + 1: i + step_size + 1])

            yield first_batch, second_batch


def main(step: int) -> None:
    with open('depth_measurements.txt') as file:
        input_text = file.read()
        measurements = list(map(int, input_text.split()))
        window = SlidingWindow(measurements)

    deeper_steps = 0
    for batch_1, batch_2 in window.go_through_window(step):
        if batch_2 > batch_1:
            deeper_steps += 1

    print(f'Total deeper steps: {deeper_steps}')


if __name__ == '__main__':
    main(1)  # puzzle 1
    main(3)  # puzzle 2
