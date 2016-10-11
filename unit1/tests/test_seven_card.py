# -*- coding: utf-8 -*-
from unit1.seven_card import best_hand

__author__ = 'Simon'


def test_best_hand():
    assert (best_hand("6C 7C 8C 9C TC 5C JS".split())
            == [['6C', '7C', '8C','9C', 'TC'], ])
    assert (best_hand("TD TC TH 7C 7D 8C 8S".split())
            == [['8C', '8S', 'TC', 'TD', 'TH'], ])
    assert (best_hand("TD TC TH 7C 7D 7S 7H".split())
            == [['7C', '7D', '7H', '7S', 'TD'],
                ['7C', '7D', '7H', '7S', 'TC'],
                ['7C', '7D', '7H', '7S', 'TH']])