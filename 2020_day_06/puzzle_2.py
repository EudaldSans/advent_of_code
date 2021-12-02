if __name__ == '__main__':
    with open('answers.tx') as f:
        total_questions = 0
        letters = list()
        new_line = True
        for line in f:  # read rest of lines
            questions = line.rstrip('\n')

            if not line.rstrip('\n'):
                print(letters)
                new_line = True
                total_questions += len(letters)
                letters = list()
                continue

            print(questions)

            if new_line:
                for letter in questions:
                    letters.append(letter)
                    new_line = False

                continue

            i = 0
            while i < len(letters):
                element = letters[i]
                if element not in questions:
                    del letters[i]
                else:
                    i += 1

    print(letters)
    new_line = True
    total_questions += len(letters)

    print(f'Total answered questions: {total_questions}')
