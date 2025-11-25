import math

if __name__ == '__main__':
    with open('bus_timetable.tx') as f:
        lines = f.readlines()

        time_of_arrival = int(lines[0])
        ids = lines[1].rstrip('\n').split(',')

    ids = list(filter(lambda a: a != 'x', ids))
    ids = [int(a) for a in ids]
    timetable = [math.ceil(time_of_arrival/x) for x in ids]

    next_stop_of_busses = [(x*y) - time_of_arrival for x, y in zip(timetable, ids)]

    time_for_next_bus = min(next_stop_of_busses)
    id_of_next_bus = ids[next_stop_of_busses.index(time_for_next_bus)]

    print(f'Next bus id {id_of_next_bus} will pass in {time_for_next_bus} minutes. Result {id_of_next_bus*time_for_next_bus}')

