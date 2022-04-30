

if __name__ == '__main__':
    start = 284639
    finish = 748759

    valid_passwords = 0

    for password in range(start, finish):
        password_str = str(password)

        doubles = False
        non_decreasing = True

        previous_char = '0'

        for character in password_str:
            if previous_char == character:
                doubles = True

            if int(previous_char) > int(character):
                non_decreasing = False
                break

            previous_char = character

        if doubles and non_decreasing:
            valid_passwords += 1

    print(f'There are {valid_passwords} valid passwords between {start} and {finish}')
