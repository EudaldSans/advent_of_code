import re

byr_re = re.compile('byr:([0-9]{4})')
iyr_re = re.compile('iyr:([0-9]{4})')
eyr_re = re.compile('eyr:([0-9]{4})')
hgt_re = re.compile('hgt:([0-9]*)(cm|in)')
hcl_re = re.compile('hcl:#([0-9a-f]{6})')
ecl_re = re.compile('ecl:(amb|blu|brn|gry|grn|hzl|oth)')
pid_re = re.compile('pid:([0-9]{9})')


def check_passport(passport):
    birth = byr_re.search(passport)
    if not birth:
        return False
    elif not 1920 < int(birth.group(1)) <= 2002:
        return False

    issue_year = iyr_re.search(passport)
    if not issue_year:
        return False
    elif not 2010 <= int(issue_year.group(1)) <= 2020:
        return False

    expiration_year = eyr_re.search(passport)
    if not expiration_year:
        return False
    if not 2020 <= int(expiration_year.group(1)) <= 2030:
        return False

    height = hgt_re.search(passport)
    if not height:
        return False
    elif height.group(2) == 'cm' and not 150 <= int(height.group(1)) <= 193:
        return False
    elif height.group(2) == 'in' and not 59 <= int(height.group(1)) <= 76:
        return False

    hair_color = hcl_re.search(passport)
    if not hair_color:
        return False

    eye_color = ecl_re.search(passport)
    if not eye_color:
        return False

    passport_id = pid_re.search(passport)
    if not passport_id:
        return False

    print(f'{birth.group(0)} {issue_year.group(0)} {expiration_year.group(0)} {hair_color.group(0)} {eye_color.group(0)} {passport_id.group(0)} {height.group(0)}')

    return True


if __name__ == '__main__':
    with open('passports.tx') as f:
        new_passport = ''
        passports_found = 0
        for line in f:  # read rest of lines
            new_passport += line.rstrip('\n') + ' '
            if not line.rstrip('\n'):
                if check_passport(new_passport):
                    passports_found += 1

                new_passport = ''

        if check_passport(new_passport):
            passports_found += 1

    print(f'Found {passports_found} valid passports')
