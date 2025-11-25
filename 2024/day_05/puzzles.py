from typing import List


class UpdateRule:
    def __init__(self, page: int, preceding_pages: List[int]):
        self.current_page = page
        self.preceding_pages = preceding_pages

    def add_preceding_page(self, page: int):
        self.preceding_pages.append(page)

    def check_rule(self, update: List[int], fix_update=False) -> bool:
        if self.current_page not in update:
            return True

        index_of_current_page = update.index(self.current_page)

        for preceding_page in self.preceding_pages:
            if preceding_page in update and update.index(preceding_page) > index_of_current_page:
                if fix_update:
                    self.swap_page(update, preceding_page)
                return False

        return True

    def swap_page(self, update: List[int], preceding_page: int):
        preceding_page_idx = update.index(preceding_page)
        current_page_idx = update.index(self.current_page)

        update[preceding_page_idx] = self.current_page
        update[current_page_idx] = preceding_page


def find_middle_pages_sum(updates: List[List[int]]) -> int:
    middle_pages = [update[len(update)//2] for update in updates]
    return sum(middle_pages)


def main(ordering_rules_file_name: str):
    with open(ordering_rules_file_name, 'r') as f:
        lines = f.readlines()

    page_ordering_rules = dict()
    updates_to_produce = list()

    found_separator = False

    for line in lines:
        if line == '\n':
            found_separator = True
            continue

        if found_separator:
            updates_to_produce.append([int(page) for page in line.rstrip('\n').split(',')])

        else:
            page_1, page_2 = line.rstrip('\n').split('|')

            page_1 = int(page_1)
            page_2 = int(page_2)

            if page_ordering_rules.get(page_2) is None:
                page_ordering_rules[page_2] = UpdateRule(page_2, [page_1])
            else:
                page_ordering_rules[page_2].add_preceding_page(page_1)

    correct_updates = list()
    incorrect_updates = list()

    for update in updates_to_produce:
        update_is_correct = True

        for page in update:
            current_rule = page_ordering_rules.get(page)

            if current_rule is not None and not current_rule.check_rule(update):
                update_is_correct = False
                break

        if update_is_correct:
            correct_updates.append(update)
        else:
            incorrect_updates.append(update)

    print(f'Sum of middle pages of ordered updates: {find_middle_pages_sum(correct_updates)}')

    for update in incorrect_updates:
        recheck_update = True

        while recheck_update:
            recheck_update = False

            for page in update:
                current_rule = page_ordering_rules.get(page)

                if current_rule is not None:
                    while not current_rule.check_rule(update, True):
                        recheck_update = True
                        continue

    print(f'Sum of middle pages of corrected updates: {find_middle_pages_sum(incorrect_updates)}')


if __name__ == '__main__':
    main('page_ordering_rules.txt')
