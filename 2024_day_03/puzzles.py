import re

mul_re = re.compile(r'mul\((\d{1,3}),(\d{1,3})\)')

do_re = re.compile(r"(do\(\))")
dont_re = re.compile(r"(don't\(\))")

all_re = re.compile(r"(don't\(\)|do\(\)|mul\(\d{1,3},\d{1,3}\))")

def main(code_file:str):
    with open(code_file, 'r') as f:
        code_lines = f.readlines()

    result = 0

    for line in code_lines:
        mul_instructions = mul_re.findall(line)
        mul_instructions = [[int(a), int(b)] for a, b in mul_instructions]

        for a, b in mul_instructions:
            result += a * b

    print(f'The result of all mul operations is {result}')

    result = 0
    mul_operation_active = True
    for line in code_lines:

        for match in all_re.finditer(line):
            sub_string = match.group()

            if sub_string == 'do()':
                print('is do')
                mul_operation_active = True

            elif sub_string == "don't()":
                print('is dont')
                mul_operation_active = False

            elif mul_operation_active:
                print(f'is mul {mul_re.match(sub_string)}')
                a, b = mul_re.findall(sub_string)[0]
                result += int(a) * int(b)

    print(f'The result of all allowed mul operations is {result}')


if __name__ == '__main__':
    main('code_lines.txt')

