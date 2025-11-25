

def card_to_num(card: str, j_value: int = 11) -> int:
    if card.isnumeric(): return int(card)

    match card:
        case 'T': return 10
        case 'J': return j_value
        case 'Q': return 12
        case 'K': return 13
        case 'A': return 14

        case _: raise ValueError(f'Invalid card {card}')


def get_hand_type(hand: str, use_jokers: bool = False) -> int:
    if use_jokers:
        if hand == 'JJJJJ': return 6

        letter_appearances = [hand.count(letter) for letter in hand if letter != 'J']
        joker_appearances = hand.count('J')

        max_appearances = max(letter_appearances) + joker_appearances

    else:
        letter_appearances = [hand.count(letter) for letter in hand]

        max_appearances = max(letter_appearances)

    if max_appearances == 5: return 6
    elif max_appearances == 4: return 5
    elif max_appearances == 3 and min(letter_appearances) == 2: return 4
    elif max_appearances == 3: return 3
    elif max_appearances == 2 and sum(letter_appearances) == 9: return 2
    elif max_appearances == 2: return 1
    else: return 0


class PokerHand:
    def __init__(self, hand: str, bid: int) -> None:
        self.hand_str = hand
        self.hand = [card_to_num(card) for card in hand]
        self.bid = bid
        self.type = get_hand_type(hand)

    def __repr__(self):
        return f'Hand {self.hand_str} of type {self.type} with repr {self.hand}'

    def __eq__(self, other: 'PokerHand') -> bool:
        return self.hand == other.hand

    def _ne__(self, other: 'PokerHand') -> bool:
        return self.hand != other.hand

    def __gt__(self, other: 'PokerHand') -> bool:
        if self.type > other.type: return True
        if self.type < other.type: return False

        cards_values = zip(self.hand, other.hand)
        for my_value, other_value in cards_values:
            if my_value > other_value: return True
            if my_value < other_value: return False

        return False

    def __ge__(self, other: 'PokerHand') -> bool:
        if self == other: return True
        else: return self > other

    def __lt__(self, other) -> bool:
        if self.type < other.type: return True
        if self.type > other.type: return False

        cards_values = zip(self.hand, other.hand)
        for my_value, other_value in cards_values:
            if my_value < other_value: return True
            if my_value > other_value: return False

        return False

    def __le__(self, other: 'PokerHand') -> bool:
        if self == other: return True
        else: return self < other


def type_to_name(type: int) -> str:
    match type:
        case 0: return 'high card'
        case 1: return 'pair'
        case 2: return 'double pair'
        case 3: return 'triple'
        case 4: return 'full house'
        case 5: return 'four of a kind'
        case 6: return 'five of a kind'

        case _: return 'unknown'


class UpdatedPokerHand(PokerHand):
    def __init__(self, hand: str, bid: int) -> None:
        super().__init__(hand, bid)
        self.type = get_hand_type(hand)
        self.hand = [card_to_num(card, j_value=1) for card in hand]


def main(file_name: str) -> None:
    with open(file_name, 'r') as hands_file:
        card_hands = [line.strip('\n').split(' ') for line in hands_file.readlines()]

    updated_card_hands = [UpdatedPokerHand(hand, int(bid)) for hand, bid in card_hands]
    updated_card_hands.sort()

    card_hands = [PokerHand(hand, int(bid)) for hand, bid in card_hands]
    card_hands.sort()

    result = 0
    for count, card in enumerate(card_hands, start=1):
        result += count * card.bid

    print(result)

    result = 0
    for count, card in enumerate(updated_card_hands, start=1):
        result += count * card.bid

    print(result)


if __name__ == '__main__':
    main('hands_list.txt')
