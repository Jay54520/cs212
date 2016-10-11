# -*- coding: utf-8 -*-
## Poker Homework 1, problem 2: Jokers

## Deck add two cards:
## '?B': black joker; can be used as any black card (S or C)
## '?R': red joker; can be used as any red card (H or D)
import itertools

from unit1.best_hand import poker
from unit1.seven_card import best_hand

__author__ = 'Simon'

JOKER = {'?B': ['AC', '2C', '3C', '4C', '5C', '6C', '7C',
                '8C', '9C', 'TC', 'JC', 'QC', 'KC',
                'AS', '2S', '3S', '4S', '5S', '6S', '7S',
                '8S', '9S', 'TS', 'JS', 'QS', 'KS'],
         '?R': ['AH', '2H', '3H', '4H', '5H', '6H', '7H',
                '8H', '9H', 'TH', 'JH', 'QH', 'KH',
                'AD', '2D', '3D', '4D', '5D', '6D', '7D',
                '8D', '9D', 'TD', 'JD', 'QD', 'KD'],}


def replacements(card):
    if card in ('?B', '?R'):
        return JOKER[card]
    return [card]


def best_wild_hand(hand):
    """Try all values for jokers in all 5-card selections"""
    all_5_hands = [best_hand(h)[0]
                      for h in itertools.product(*map(replacements, hand))]
    return poker(all_5_hands)

