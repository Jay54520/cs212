# -*- coding: utf-8 -*-

__author__ = 'Simon'

Fail = []

def elapsed_time(path):
    """
    return final elapsed_time of this path
    state: (here, there, elapsed_time)
    :param path: [ (state), action, (state), action, (state) ......]
    :return:
    """
    return path[-1][-1]


def path_actions(path):
    """
    Return a list of actions  in this path.
    :param path: [ (state), action, (state), action, (state) ......]
    :return:
    """
    return path[1::2]


def path_states(path):
    """
    Return a list of states in this path.
    :param path: [ (state), action, (state), action, (state) ......]
    :return:
    """
    return path[0::2]


def bcost(action):
    """Returns the cost (a number) of an action in the bridge problem."""
    a, b, arrow = action
    return max(a, b)


def path_cost(path):
    """The total cost of path (which is stored in a tuple with the final action)."""
    if len(path) < 3:
        return 0
    else:
        return sum([bcost(action) for action in path_actions(path)])


def bsuccessors(state):
    """Return a dict of {state:action} pairs. A `state` is a (here, there, t) tuple,
    where `here` and `there` are frozensets of people (indicated by their times) and/or
    the `light`, and `t` is a number indicating the elapsed time. Action is represented
    by '->' for here to there and '<-' for there to here.
    Use `frozensets` because `frozensets` is hashable. (Each person has a individual speed)

    select two people(if people is same, then indicate one person) from here or there besides `light`
    """
    here, there, t = state
    if not here:
        return here
    successors = {}
    # if 'light' in `here`, select two people + 'light'
    if 'light' in here:
        for a in here:
            if a is not 'light':
                for b in here:
                    if b is not 'light':
                        tmp_fronzenset = frozenset([a, b, 'light'])
                        successors[(here - tmp_fronzenset, there | tmp_fronzenset, t + max(a, b) )] = ['%s, %s, light ->' % (a, b)]
    else:
        for a in there:
            if a is not 'light':
                for b in there:
                    if b is not 'light':
                        tmp_fronzenset = frozenset([a, b, 'light'])
                        successors[(here | tmp_fronzenset, there - tmp_fronzenset, t + max(a, b))] = ['%s, %s, light <-' % (a, b)]

    return successors


def bridge_problem(here):
    """

    :param here: a individual list represented minutes to pass the bridge
    :return:
    """
    # initialize, the `light` is in `here`
    here = frozenset(here) | frozenset(['light'])
    frontier = [ [(here, frozenset(), 0)], ]
    explored = set()

    if not here:
        return frontier[0]

    while frontier:
        path = frontier.pop(0)
        here, _, _ = state1 = path[-1]
        # test the result later because we will sort after path being
        # appended
        if not here:
            return path
        for state, action in bsuccessors(path[-1]).items():
            if state not in explored:
                explored.add(state)
                path2 = path + [action, state]
                here, _, _ = state
                frontier.append(path2)
                # sort by elapsed_time, then will return shortest path first
                frontier.sort(key=elapsed_time)


result = bridge_problem([1, 2, 5, 10])
print(result)
print(bsuccessors( ( frozenset([1, 2, 3, 'light']), frozenset(), 0 ) ))
