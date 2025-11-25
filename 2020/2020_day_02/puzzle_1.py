import re

if __name__ == '__main__':
    array = list()
    pattern = re.compile('([0-9]*)-([0-9]*) ([a-z]): ([a-z]*)')
    with open('passwords.tx') as f:
        total_results = 0
        for line in f:  # read rest of lines
            _, minimum, maximum, letter, password, _ = pattern.split(line)
            if int(minimum) < len(pattern.findall(letter, password)) < int(maximum):
                total_results += 1

print(f'There are {total_results} correct passwords')
