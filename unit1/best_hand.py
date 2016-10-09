# -*- coding: utf-8 -*-
import random

__author__ = 'Simon'

"""
Select best hand(s) from multiply hands according to 
Texas hold'em Poker rules.
"""
HAND_NAMES = {8: "Straight Flush",
              7: "4 of a Kind",
              6: "Full House",
              5: "Flush",
              4: "Straight",
              3: "3 of a Kind",
              2: '2 Pair',
              1: "Pair",
              0: "High Card"}


def deal(numhands, n=5, deck=[r+s for r in '23456789TJQKA' for s in 'SHDC']):
    "Shuffle the deck and deal out numhands n-card hands."
    if numhands * n > len(deck):
        raise ValueError('The deck is not enough because there are too many people.')
    random.shuffle(deck)
    return [deck[n*i:n*(i+1)] for i in range(numhands)]

def card_ranks(ranks):
    """Return a list of ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in ranks]
    ranks.sort(reverse=True)

    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight(顺子)"""
    ranks = sorted(ranks, reverse=True)
    return all(ranks[i] - 1 == ranks[i+1] for i in range(len(ranks) - 1))


def flush(hand):
    """
    Return True if all the card have the same suite(花色)
    :param hand: ['6C', '7C', '8C', '9C', 'TC']
    :return: type: bool
    """
    suite = [s for r, s in hand]
    return len(set(suite)) == 1


def kind(num, ranks):
    """Return card that have `num` of same number card in ranks.
    Return None if there is no n-of-a-kind in the ranks.
    eg: params: (3, [5, 5, 5, 3, 2]) --> 5
    eg: params: (2, [4, 4, 9, 6, 7]) --> 4
    """
    for r in ranks:
        if ranks.count(r) == num: return r
    return None


def two_pair(ranks):
    """Special `kind` with two pair
    eg: [9, 5, 5, 4, 4] --> [5, 4]
    """
    pair = kind(2, ranks)
    lowpair = kind(2, list(reversed(ranks)))
    if pair != lowpair:
        return [pair, lowpair]
    else:
        return None


def group(items):
    """eg: [7, 10, 7, 9, 7] =>  [(3, 7), (1, 10), (1, 9)] used to generate =>
    count = (3, 1, 1);  ranks = (7, 10, 9)
    The front tuple describe how many kinds of a poker, the behind describe
    corresponding poker number"""
    items_set = set(items)
    groups = [(items.count(item), item) for item in items_set]
    return sorted(groups, reverse=True)


count_rankings = {(5,): 10, (4, 1): 7, (3, 2): 6, (3, 1, 1): 3,
                  (2, 2, 1): 2, (2, 1, 1, 1): 1, (1, 1, 1, 1, 1): 0}


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    groups = group(card_ranks(hand))
    counts, ranks = zip(*groups)
    is_straight = straight(ranks)
    is_flush = flush(hand)
    return max(count_rankings[counts], 4*is_straight + 5*is_flush), ranks


def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    if not hands:
        raise ValueError('Hands must not be empty!')
    max_ranking = max(hand_rank(hand) for hand in hands)
    return [hand for hand in hands if hand_rank(hand) == max_ranking]


def hand_percentages(n=700*1000):
    """Sample n random hands and print a table of percentages for each type of hand."""
    counts = [0] * 9
    for i in range(n//10):
        for hand in deal(10):
            ranking = hand_rank(hand)[0]
            counts[ranking] += 1
    for i in reversed(range(0, 9)):
        print("%14s: %6.4f %%" % (HAND_NAMES[i], 100*counts[i]/n))


if __name__ == '__main__':
    print(hand_rank("6C 7C 8C 9C TC".split()))