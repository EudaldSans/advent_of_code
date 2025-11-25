from typing import List, Union, Tuple
from copy import deepcopy


def find_next_free_spot(start: int, disk: List[Union[int, str]], min_length: int) -> Tuple[int,int]:
    first_free_space = len(disk) - 1
    free_space_length = 0
    found_free_space = False

    for count, byte in enumerate(disk[start:]):
        if byte == '.' and not found_free_space:
            first_free_space = count
            found_free_space = True

        if found_free_space and byte != '.':
            free_space_length = count - first_free_space
            if free_space_length >= min_length:
                break
            else:
                found_free_space = False

    return first_free_space + start, free_space_length


def find_next_file(start: int, disk: List[Union[int, str]]) -> Tuple[int, int]:
    first_file_pos = -1
    file_length = 0
    found_file = False

    disk_size = len(disk)
    file_end = disk_size
    start_byte = '.'

    for count, byte in enumerate(reversed(disk[:start])):
        byte_pos = disk_size - count - 1

        if byte != '.' and not found_file:
            file_end = byte_pos
            found_file = True
            start_byte = byte

        if found_file and byte != start_byte:
            file_length = file_end - byte_pos
            first_file_pos = byte_pos + 1

            break

    return first_file_pos, file_length


def get_checksum(disk: List[Union[int, str]]) -> int:
    checksum = 0

    for position, file_id in enumerate(disk):
        if file_id == '.':
            break

        checksum += position * file_id

    return checksum


def main(disk_file: str):
    with open(disk_file, 'r') as f:
        disk_str = f.readline().rstrip('\n')

    disk_files = [int(value) for value in disk_str]
    disk_size = sum(disk_files)

    print(f'{disk_size=}')

    disk = ['.'] * disk_size
    print(disk)

    pointer = 0
    file_id = 0
    for count, file_size in enumerate(disk_files):
        if count % 2 == 1:  # Free space
            pointer += file_size
        else:  # File
            disk[pointer:pointer + file_size] = [file_id] * file_size
            file_id += 1
            pointer += file_size

    next_free_space, _ = find_next_free_spot(0, disk, 1)

    print(disk)
    disk_1 = deepcopy(disk)

    for count, byte in enumerate(reversed(disk_1)):
        byte_pos = disk_size - count - 1
        if byte == '.':
            continue

        if byte_pos <= next_free_space:
            break

        if disk_1[next_free_space] != '.':
            next_free_space, _ = find_next_free_spot(next_free_space, disk_1, 1)

        disk_1[next_free_space], disk_1[byte_pos] = disk_1[byte_pos], disk_1[next_free_space]
        next_free_space += 1

    print(disk_1)
    print(f'The checksum is {get_checksum(disk_1)}')

    disk_2 = deepcopy(disk)

    next_fs = 0
    next_f = disk_size - 1

    next_f, f_length = find_next_file(next_f, disk_2)

    while True:
        next_fs, fs_length = find_next_free_spot(0, disk_2, f_length)

        if fs_length != -1 and next_f > next_fs:
            disk_2[next_fs: next_fs + f_length], disk_2[next_f: next_f + f_length] = (
                disk_2[next_f: next_f + f_length], disk_2[next_fs: next_fs + f_length])

            print(disk_2)

        elif next_f < next_fs:
            break

        next_f, f_length = find_next_file(next_f, disk_2)

        if next_fs + fs_length >= len(disk_2) - 1:
            break

    print(disk_2)
    print(f'The checksum is {get_checksum(disk_2)}')


def getc(size, timeout=1):
    return 'C'


def putc(data, timeout=1):
    print(data)
    return True  # note that this ignores the timeout


if __name__ == '__main__':
    main('example_2.txt')

