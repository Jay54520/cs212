# -*- coding: utf-8 -*-

__author__ = 'Simon'

"""
https://en.wikipedia.org/wiki/Liquid_water_pouring_puzzles

thinking:
How to describe all the status of glass, water and etc
volume of glass
empty, full of glass
transfer(a_glass, b_glass)
    X -> Y
    1. until Y is full
    2. until X is empty

:return a sequence of steps between glasses
complexity: Can't tell because it's a sequence of steps
<b>search</b> problem

1. don't reverse
selected 2. shortest first
selected 3. don't re-explore

help:
python list concatenate:

>>> [[0, 0]] + ['fill X']
[[0, 0], 'fill X']
>>> [[0, 0]] + ['fill X', (4, 0)]
[[0, 0], 'fill X', (4, 0)]

"""
Fail = []

def successors(x, y, X, Y):
    """Return a dict of {action:state} pairs describing what can
    be reached from the (x, y) state, and how."""
    assert x <= X
    assert y <= Y
    result = {
        'fill X': (X, y),
        'Y->X': (X, y-(X - x)) if x + y >= X else (x + y, 0),
        'X->Y': (x - (Y - y), Y) if x + y >= Y else (0, x + y),
        'empty X': (0, y),
        'empty Y': (x, 0),
        'fill Y': (x, Y)
    }
    return result


def pour_problem(X, Y, goal, start=(0, 0)):
    """
    X and Y are the capacity of glasses; (x, y) is current fill
    levels and represents a state. The goal is a level that can be in either
    glass. Start at start state and follow successors until we reach
    the goal. Keep track of frontier and previously explored; fail when no
    frontier.
    """
    if goal > max(X, Y):
        raise ValueError('goal: %s greater than max(%s, %s)' % (goal, X, Y))
    if goal in start:
        return goal
    frontier = [ [start], ]
    explored = set()
    explored.add(start)
    while frontier:
        path = frontier.pop(0)
        x, y = path[-1]
        for (action, state) in successors(x, y, X, Y).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                if goal in state:
                    return path2
                else:
                    frontier.append(path2)

    return Fail
