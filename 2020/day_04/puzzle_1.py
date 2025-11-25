import re


patterns = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid', 'cid']


def check_passport(passport):
    for pattern in patterns:
        if pattern == 'cid':
            continue
        if re.search(pattern, passport) is None:
            return False

    return True


if __name__ == '__main__':
    with open('passports.tx') as f:
        new_passport = ''
        passports_found = 0
        for line in f:  # read rest of lines
            new_passport += line.rstrip('\n')
            if not line.rstrip('\n'):
                if check_passport(new_passport):
                    passports_found += 1

                new_passport = ''

        if check_passport(new_passport):
            passports_found += 1

    print(f'Found {passports_found} valid passports')