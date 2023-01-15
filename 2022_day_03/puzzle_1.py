

def main():
    with open('rucksacks.txt') as rucksacks_file:
        rucksacks = [rucksack.rstrip('\n') for rucksack in rucksacks_file.readlines()]

    priority_sum = 0

    for rucksack in rucksacks:
        rucksack_size = len(rucksack)

        compartment_1 = rucksack[:rucksack_size//2]
        compartment_2 = rucksack[rucksack_size//2:]

        for item in compartment_1:
            if item in compartment_2:
                if ord(item) < ord('a'):
                    priority_sum += ord(item) - ord('A') + 27
                else:
                    priority_sum += ord(item) - ord('a') + 1

                break

    print(f'Total priorities: {priority_sum}')


if __name__ == '__main__':
    main()
