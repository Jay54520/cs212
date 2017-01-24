# -*- coding: utf-8 -*-

__author__ = 'Simon'


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A `state` is a (here, there, t) tuple,
    where `here` and `there` are frozensets of people (indicated by their times) and/or
    the `light`, and `t` is a number indicating the elapsed time. Action is represented
    by '->' for here to there and '<-' for there to here.
    Use `frozensets` because `frozensets` is hashable and two people with same
     minutes can be considered as same person
    """
    here, there, t = state
    result = {}
    if 'light' in here:
        for a in here:
            if a is not 'light':
                for b in here:
                    if b is not 'light':
                        result[
                            (here - frozenset([a, b, 'light']),
                             there | frozenset([a, b, 'light']),
                             t + max(a, b)
                             )] = (a, b, '->')
    else:
        for a in there:
            if a is not 'light':
                for b in there:
                    if b is not 'light':
                        result[
                            (here | frozenset([a, b, 'light']),
                             there - frozenset([a, b, 'light']),
                             t + max(a, b)
                             )] = (a, b, '<-')
    return result


def elapsed_time(path):
    return path[-1][2]


def bridge_problem(here):
    here = frozenset(here) | frozenset(['light'])
    explored = set()
    frontier = [ [(here, frozenset(), 0)], ]
    if not here:
        return frontier[0]

    while frontier:
        path = frontier.pop(0)
        for (state, action) in bsuccessors(path[-1]).items():
            if state not in explored:
                explored.add(state)
                here, there, t = state
                path2 = path + [action, state]
                if not here:
                    return path2
                else:
                    frontier.append(path2)
                    frontier.sort(key=elapsed_time)


result = bridge_problem([1, 2, 5, 10])
print(result[1::2])
print(result)
