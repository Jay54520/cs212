# -*- coding: utf-8 -*-
import doctest

from unit4.bridge_problem import *

__author__ = 'Simon'


class TestBridge:
    """
>>> path_actions(bridge_problem([1,2,5,10]))
[['2, 1, light ->'], ['1, 1, light <-'], ['5, 10, light ->'], ['2, 2, light <-'], ['2, 1, light ->']]
>>> path_actions(bridge_problem([1,2,5,10, 15, 20]))
[['2, 1, light ->'], ['1, 1, light <-'], ['10, 5, light ->'], ['2, 2, light <-'], ['2, 1, light ->'], ['1, 1, light <-'], ['15, 20, light ->'], ['2, 2, light <-'], ['2, 1, light ->']]
>>> path_actions(bridge_problem([1,2,4,8, 16, 33]))
[['2, 1, light ->'], ['1, 1, light <-'], ['8, 4, light ->'], ['2, 2, light <-'], ['2, 1, light ->'], ['1, 1, light <-'], ['33, 16, light ->'], ['2, 2, light <-'], ['2, 1, light ->']]
    """

print(doctest.testmod())