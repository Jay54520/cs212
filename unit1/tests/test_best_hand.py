# -*- coding: utf-8 -*-
from unit1.best_hand import poker, hand_rank, card_ranks, straight, flush, kind, two_pair

__author__ = 'Simon'


def test_poker():
    """"Test cases for the functions in the poker program."""
    sf = "6C 7C 8C 9C TC".split()  # Straight Flush (同花顺)
    fk = "9D 9H 9S 9C 7D".split()  # Four of a kind (四条)
    fh = "TD TC TH 7C 7D".split()  # Full House (骷髅)
    tp = "5S 5D 9H 9C 6S".split()  # 双对
    fkranks = card_ranks(fk)
    tpranks = card_ranks(tp)

    assert kind(4, fkranks) == 9
    assert kind(3, fkranks) == None
    assert kind(2, fkranks) == None
    assert kind(1, fkranks) == 7

    assert two_pair(fkranks) == None
    assert two_pair(tpranks) == [9, 5]

    assert straight([10, 9, 8, 7, 6]) == True
    assert straight([9, 9, 9, 9, 7]) == False

    assert flush(sf) == True
    assert flush(fk) == False

    assert card_ranks(sf) == [10, 9, 8, 7, 6]
    assert card_ranks(fk) == [9, 9, 9, 9, 7]
    assert card_ranks(fh) == [10, 10, 10, 7, 7]

    assert poker([sf, fk, fh]) == sf
    assert poker([fk, fh]) == fk
    assert poker([fh, fh]) == fh
    assert poker([fh]) == fh
    assert poker([sf] + 99 * [fh]) == sf

    assert hand_rank(sf) == (8, 10)
    assert hand_rank(fk) == (7, 9, 7)
    assert hand_rank(fh) == (6, 10, 7)
