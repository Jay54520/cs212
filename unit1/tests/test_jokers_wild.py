# -*- coding: utf-8 -*-
from unit1.jokers_wild import best_wild_hand

__author__ = 'Simon'


def test_best_wild_hand():
    assert (best_wild_hand("6C 7C 8C 9C TC 5C ?B".split())
            == [['7C', '8C', '9C', 'JC', 'TC'],])
    assert (best_wild_hand("TD TC 5H 7C 7D ?R ?B".split())[1]
            == ['7C', 'TC', 'TD', 'TH', 'TS'])
    assert (best_wild_hand("TD TC TH 7C 7D 7S 7H".split())
            == [['7C', '7D', '7H', '7S', 'TD'], ])