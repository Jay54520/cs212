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
"""


def successors(x, y, X, Y):
    """Return a dict of {state:action} pairs describing what can
    be reached from the (x, y) state, and how."""
    assert x <= X and y <= Y
    result = {
        # transfer from X --> Y while Y is full
        (0, y + x) if x + y <= Y else (x - (Y - y), Y): 'X->Y',
        # transfer from Y --> X while  is full
        (x+y, 0) if x + y <= X else (X, y - (X - x)): 'Y->X',
        (X, y): 'fill X',
        (0, y): 'empty X',
        (x, Y): 'fill Y',
        (x, 0): 'empty Y',
    }
    return result


def pour_problem(X, Y, goal, start=(0, 0)):
    """
    X and Y are the capcity of glasses; (x, y) is current fill
    levels and represents a state. The goal is a level that can be in either
    glass. state at state state and follow successors until we reach 
    the goal. Keep track of frontier and previously explored; fail when no
    frontier.
    :param X: 
    :param Y: 
    :param goal: 
    :param state: 
    :return: 
    """
    if goal in start:
        return goal
    explored = set()
    frontier = [[start]]  # how this work? Through all successors
    route = 0
    while frontier:
        print('frontier: %s' % frontier)
        path = frontier.pop(0)
        print('path: %s' % path)
        x, y = path[-1]
        print('x: %s; y: %s' % (x, y))
        for (state, action) in successors(x, y, X, Y).items():
            route += 1
            print('state: %s; action: %s' % (state, action))
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                print('path2: %s \n\n' % path2)
                if goal in state:
                    print('route: %s' % route)
                    return path2
                else:
                    frontier.append(path2)
    print('route: %s' % route)
    return Fail


Fail = []
print(pour_problem(4, 9, 6))

