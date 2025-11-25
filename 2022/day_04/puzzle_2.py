

def main():
    with open('tasks.txt') as rucksacks_file:
        tasks = [rucksack.rstrip('\n') for rucksack in rucksacks_file.readlines()]

    total_overlapping_tasks = 0

    for task in tasks:
        task_1, task_2 = task.split(',')

        task_1 = [int(edge) for edge in task_1.split('-')]
        task_2 = [int(edge) for edge in task_2.split('-')]

        if task_1[0] <= task_2[0] <= task_1[1] or task_1[0] <= task_2[0] <= task_1[1]:
            print(f'{task_1=}, {task_2=}')
            total_overlapping_tasks += 1

        elif task_2[0] <= task_1[0] <= task_2[1] or task_2[0] <= task_1[1] <= task_2[1]:
            print(f'{task_1=}, {task_2=}')
            total_overlapping_tasks += 1

    print(f'Total overlapping tasks: {total_overlapping_tasks}')


if __name__ == '__main__':
    main()
