# -*- coding: utf-8 -*-
import doctest

from unit4.bridge_problem import *

__author__ = 'Simon'


class TestBridge:
    """
>>> elapsed_time(bridge_problem([1,2,5,10]))
17
>>> ## There are two equally good solutions
...
>>> S1 = [(2, 1, '->'), (1, 1, '<-'), (5, 10, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> S2 = [(2, 1, '->'), (2, 2, '<-'), (5, 10, '->'), (1, 1, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,5,10])) in (S1, S2)
True
>>> path_actions(bridge_problem([1,2,5,10, 15, 20]))
[(2, 1, '->'), (1, 1, '<-'), (10, 5, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (15, 20, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> path_actions(bridge_problem([1,2,4,8, 16, 33]))
[(2, 1, '->'), (1, 1, '<-'), (8, 4, '->'), (2, 2, '<-'), (2, 1, '->'), (1, 1, '<-'), (33, 16, '->'), (2, 2, '<-'), (2, 1, '->')]
>>> [elapsed_time(bridge_problem([1, 2, 4, 8, 16][:N])) for N in range(6)]
[0, 1, 2, 7, 15, 28]
>>> [elapsed_time(bridge_problem([1, 1, 2, 3, 4, 8, 16, 44][:N])) for N in range(9)]
[0, 1, 1, 2, 6, 11, 19, 32, 68]

    """

print(doctest.testmod())