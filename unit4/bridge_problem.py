# -*- coding: utf-8 -*-

__author__ = 'Simon'

Fail = []

def elapsed_time(result):
    return result[-1][-1]


def path_actions(result):
    return result[1::2]


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
        here1, there1, t1 = state1 = path[-1]
        if not here1 or here1 == set(['light']):
            # the job is done!
            return path

        for (state, action) in bsuccessors(state1).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                frontier.append(path2)
                # combine this sort and pop(0) above, so it can
                # when meet conditions, path will be shortest
                frontier.sort(key=elapsed_time)

    return Fail

result = bridge_problem([1, 2, 5, 10])
print(result)
