# -*- coding: utf-8 -*-

__author__ = 'Simon'

"""
Select best hand(s) from multiply hands according to 
Texas hold'em Poker rules.
"""


def card_ranks(ranks):
    """Return a list of ranks, sorted with higher first."""
    ranks = ['--23456789TJQKA'.index(r) for r, s in ranks]
    ranks.sort(reverse=True)

    return [5, 4, 3, 2, 1] if (ranks == [14, 5, 4, 3, 2]) else ranks


def straight(ranks):
    """Return True if the ordered ranks form a 5-card straight(顺子)"""
    ranks.sort(reverse=True)
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


def hand_rank(hand):
    """Return a value indicating the ranking of a hand."""
    ranks = card_ranks(hand)
    if straight(ranks) and flush(hand):
        return (8, max(ranks))
    elif kind(4, ranks):
        return (7, kind(4, ranks), kind(1, ranks))
    elif kind(3, ranks) and kind(2, ranks):
        return (6, kind(3, ranks), kind(2, ranks))
    elif flush(hand):
        return (5, ranks)
    elif straight(ranks):
        return (4, max(ranks))
    elif kind(3, ranks):
        return (3, kind(3, ranks), ranks)
    elif two_pair(ranks):
        return (3, two_pair(2, ranks), ranks)
    elif kind(1, ranks):
        return (1, kind(1, ranks), ranks)
    else:
        return (0, ranks)


def poker(hands):
    "Return the best hand: poker([hand, ...]) => hand"
    if not hands:
        raise ValueError('Hands must not be empty!')
    return max(hands, key=hand_rank)