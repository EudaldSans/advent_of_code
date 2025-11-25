import re

bags_re = re.compile('([a-z]+ [a-z]+) bags contain (.+)')
rules_re = re.compile('([0-9]+) ([a-z]+ [a-z]+)')

my_color = 'shiny gold'


class Bag:
    def __init__(self, string):
        self.color = bags_re.match(string).group(1)
        rules_string = bags_re.match(string).group(2)
        rules_list = rules_re.findall(rules_string)

        self.rules = [{'color': rule[1], 'quantity': rule[0]} for rule in rules_list]
        self.color_list = [rule[1] for rule in rules_list]

    def __repr__(self):
        return f'{self.color} bag'

    def can_contain_bag(self, color):
        return color in self.color_list


def remove_bags_from_list(list, bags_to_remove):
    for bag in bags_to_remove:
        list.remove(bag)
    return list


if __name__ == '__main__':
    with open('rules.tx') as f:
        total_questions = 0
        bags = list()
        for line in f:  # read rest of lines
            bags.append(Bag(line.rstrip('\n')))

    found_bags = 0
    bags_to_check = list()
    for bag in bags:
        if bag.can_contain_bag(my_color):
            bags_to_check.append(bag)

    found_bags += len(bags_to_check)

    while bags_to_check:
        bags = remove_bags_from_list(bags, bags_to_check)
        new_bags_to_check = list()
        for bag_to_check in bags_to_check:
            for bag in bags:
                if bag.can_contain_bag(bag_to_check.color) and bag not in new_bags_to_check:
                    new_bags_to_check.append(bag)

        found_bags += len(new_bags_to_check)
        bags_to_check = new_bags_to_check

    print(f'Found {found_bags} bags that can contain {my_color}.')
