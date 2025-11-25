
# Rock beats Scissors, Paper beats Rock, Scissors beat paper
beats = {'A': 'C', 'B': 'A', 'C': 'B'}
is_beaten_by = {'A': 'B', 'B': 'C', 'C': 'A'}
points_per_move = {'A': 1, 'B': 2, 'C': 3}


def main():
    with open('directions.txt') as items_file:
        directions = items_file.readlines()

    total_points = 0

    for round in directions:
        opponent_move = round[0]
        needed_result = round[2]

        round_result = 'unknown'
        my_move = 'unknown'

        match needed_result:
            case 'X':  # lose
                my_move = beats[opponent_move]
                round_points = points_per_move[my_move]
                round_result = 'loss'

            case 'Y':  # draw
                my_move = opponent_move
                round_points = points_per_move[my_move] + 3
                round_result = 'draw'

            case 'Z':  # win
                my_move = is_beaten_by[opponent_move]
                round_points = points_per_move[my_move] + 6
                round_result = 'win'

        total_points += round_points
        print(f'Round results in {round_result}. I play {my_move}, opponent plays {opponent_move}. Round points {round_points}')

    print(f'Total points: {total_points}')


if __name__ == '__main__':
    main()