import re

bags_re = re.compile('([a-z]+ [a-z]+) bags contain (.+)')
rules_re = re.compile('([0-9]+) ([a-z]+ [a-z]+)')

my_color = 'shiny gold'


class Bag:
    def __init__(self, string):
        self.color = bags_re.match(string).group(1)
        rules_string = bags_re.match(string).group(2)
        rules_list = rules_re.findall(rules_string)

        self.rules = {rule[1]: int(rule[0]) for rule in rules_list}
        self.color_list = [rule[1] for rule in rules_list]

    def __repr__(self):
        return f'{self.color} bag'

    def can_contain_bag(self, color):
        return color in self.color_list

    def find_bags_within(self, bag_list):
        bags_within = 0
        for bag in bag_list:
            if bag.color in self.color_list:
                number_of_bags = self.rules[bag.color]

                bags_within += number_of_bags*(bag.find_bags_within(bag_list) + 1)

        return bags_within


if __name__ == '__main__':
    with open('rules.tx') as f:
        total_questions = 0
        bags = list()
        for line in f:  # read rest of lines
            new_bag = Bag(line.rstrip('\n'))
            bags.append(new_bag)

            if new_bag.color == my_color:
                my_bag = new_bag

    bags_within_my_bag = my_bag.find_bags_within(bags)

    print(f'There are {bags_within_my_bag} bags within my bag')
