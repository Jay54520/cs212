# -*- coding: utf-8 -*-

__author__ = 'Simon'

import doctest

from unit4 import *


class Test:
    """
    >>> successors(0, 0, 4, 9)
    {'fill X': (4, 0), 'Y->X': (0, 0), 'X->Y': (0, 0), 'empty X': (0, 0), 'empty Y': (0, 0), 'fill Y': (0, 9)}
    >>> successors(3, 5, 4, 9)
    {'fill X': (4, 5), 'Y->X': (4, 4), 'X->Y': (0, 8), 'empty X': (0, 5), 'empty Y': (3, 0), 'fill Y': (3, 9)}
    >>> successors(3, 7, 4, 9)
    {'fill X': (4, 7), 'Y->X': (4, 6), 'X->Y': (1, 9), 'empty X': (0, 7), 'empty Y': (3, 0), 'fill Y': (3, 9)}
    >>> pour_problem(4, 9, 6)
    [(0, 0), 'fill Y', (0, 9), 'Y->X', (4, 5), 'empty X', (0, 5), 'Y->X', (4, 1), 'empty X', (0, 1), 'Y->X', (1, 0), 'fill Y', (1, 9), 'Y->X', (4, 6)]
    >>> def num_actions(triplet):
    ...     X, Y, goal = triplet
    ...     return len(pour_problem(X, Y, goal))
    ...
    >>> def hardness(triplet):
    ...     X, Y, goal = triplet
    ...     return num_actions((X, Y, goal))
    ...
    >>> max([(X, Y, goal) for X in range(1, 10) for Y in range(1, 10)
    ...                     for goal in range(1, max(X, Y))], key=num_actions)
    (7, 9, 8)
    >>> pour_problem(7, 9, 8)
    [(0, 0), 'fill Y', (0, 9), 'Y->X', (7, 2), 'empty X', (0, 2), 'Y->X', (2, 0), 'fill Y', (2, 9), 'Y->X', (7, 4), 'empty X', (0, 4), 'Y->X', (4, 0), 'fill Y', (4, 9), 'Y->X', (7, 6), 'empty X', (0, 6), 'Y->X', (6, 0), 'fill Y', (6, 9), 'Y->X', (7, 8)]
    >>> len(pour_problem(7, 9, 8))
    29
    """


print(doctest.testmod())
