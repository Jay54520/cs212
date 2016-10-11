# -*- coding: utf-8 -*-
## Poker Homework 1, problem 2: Jokers

## Deck add two cards:
## '?B': black joker; can be used as any black card (S or C)
## '?R': red joker; can be used as any red card (H or D)
import itertools

from unit1.best_hand import poker
from unit1.seven_card import best_hand

__author__ = 'Simon'

allranks = 'A23456789TJQK'
redcards = [r+s for r in allranks for s in 'DH']
blackcards = [r+s for r in allranks for s in 'SC']
JOKER = {'?B': blackcards,
         '?R': redcards,}


def replacements(card):
    if card in ('?B', '?R'):
        return JOKER[card]
    return [card]


def best_wild_hand(hand):
    """Try all values for jokers in all 5-card selections"""
    all_5_hands = [best_hand(h)[0]
                      for h in itertools.product(*map(replacements, hand))]
    return poker(all_5_hands)

