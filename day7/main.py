from collections import Counter
from dataclasses import dataclass
from enum import IntEnum
from typing import Self

class HandType(IntEnum):
    HIGH = 0
    PAIR = 1
    TWO_PAIR = 2
    THREE_KIND = 4
    FULL_HOUSE = 5
    FOUR_KIND = 6
    FIVE_KIND = 7

    def get_type(hand: str) -> Self:
        cards = [v for v in Counter(hand).values()]
        if 5 in cards:
            return HandType.FIVE_KIND
        if 4 in cards:
            return HandType.FOUR_KIND
        if 3 in cards and 2 in cards:
            return HandType.FULL_HOUSE
        if 3 in cards:
            return HandType.THREE_KIND
        if cards.count(2) == 2:
            return HandType.TWO_PAIR
        if 2 in cards:
            return HandType.PAIR
        return HandType.HIGH

vals = "23456789TJQKA"
def get_type(hand: str) -> HandType:
    return HandType.get_type(hand)

@dataclass
class Hand:
    hand: str
    bid: int
    hand_type: HandType

    def __init__(self, hand: str, bid: int) -> None:
        self.hand = hand
        self.bid = bid
        self.hand_type = get_type(hand)

    def __lt__(self, other: Self) -> bool:
        if self.hand_type != other.hand_type:
            return self.hand_type < other.hand_type
        for i in range(len(self.hand)):
            if self.hand[i] != other.hand[i]:
                return vals.index(self.hand[i]) < vals.index(other.hand[i])

hands: list[Hand] = []
with open("i.txt") as f:
    for l in f.readlines():
        h, b = l.split(" ")
        hands.append(Hand(h, int(b)))

# part 1
hands.sort()
res = 0
for i in range(len(hands)):
    res += hands[i].bid * (i + 1)
print(res)


# part 2
vals = "J23456789TQKA"
def get_type(hand: str) -> HandType:
    # we still want to consider the original where J is just a normal card and not joker????? why?????
    possible_hands: list[str] = [hand]
    uniqe_cards = [c for c in hand if c != "J"]
    for c in uniqe_cards:
        possible_hands.append(hand.replace("J", c))

    hand_type = HandType.HIGH
    for h in possible_hands:
        hand_type = max(hand_type, HandType.get_type(h))
    return hand_type

# call get_type on all hands again to update it 
hands = [Hand(h.hand, h.bid) for h in hands]
hands.sort()
res = 0
for i in range(len(hands)):
    res += hands[i].bid * (i + 1)
print(res)