import numpy as np


def main():
    with open('rucksacks.txt') as rucksacks_file:
        rucksacks = [rucksack.rstrip('\n') for rucksack in rucksacks_file.readlines()]

    priority_sum = 0
    elf_gropus = np.array_split(rucksacks, len(rucksacks)//3)

    for elf_1, elf_2, elf_3 in elf_gropus:
        for item in elf_1:
            if item in elf_2 and item in elf_3:
                if ord(item) < ord('a'):
                    priority_sum += ord(item) - ord('A') + 27
                else:
                    priority_sum += ord(item) - ord('a') + 1

                break

    print(f'Total priorities: {priority_sum}')


if __name__ == '__main__':
    main()
