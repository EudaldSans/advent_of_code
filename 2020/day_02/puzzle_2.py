import re

if __name__ == '__main__':
    array = list()
    pattern = re.compile('([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)')
    with open('passwords.tx') as f:
        total_results = 0
        for line in f:  # read rest of lines
            _, pos1, pos2, letter, password, _ = pattern.split(line)
            pos1 = int(pos1)-1
            pos2 = int(pos2)-1
            if password[pos1] == letter != password[pos2] or password[pos1] != letter == password[pos2]:
                total_results += 1

print(f'There are {total_results} correct passwords')