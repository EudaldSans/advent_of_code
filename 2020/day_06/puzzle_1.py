if __name__ == '__main__':
    with open('answers.tx') as f:
        total_questions = 0
        letters = list()
        for line in f:  # read rest of lines
            questions = line.rstrip('\n')

            for letter in questions:
                if letter not in letters:
                    total_questions += 1
                    letters.append(letter)

            if not line.rstrip('\n'):
                letters = list()

    print(f'Total answered questions: {total_questions}')
