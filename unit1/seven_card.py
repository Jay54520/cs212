# -*- coding: utf-8 -*-
# Poker Homework 1, problem 1: 7-card stud
import itertools

from unit1.best_hand import poker

__author__ = 'Simon'


def best_hand(hand):
    """From a 7-card hand, return the best 5 card hand"""
    all_5_hands = list(itertools.combinations(hand, 5))
    best_hands = poker(all_5_hands)
    return best_hands
