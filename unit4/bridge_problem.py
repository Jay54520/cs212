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
        return path[-2][-1]


def bsuccessors(state, t):
    """Return a dict of {state:action} pairs. A `state` is a (here, there, t) tuple,
    where `here` and `there` are frozensets of people (indicated by their times) and/or
    the `light`, and `t` is a number indicating the elapsed time. Action is represented
    by '->' for here to there and '<-' for there to here.
    Use `frozensets` because `frozensets` is hashable. (Each person has a individual speed)

    select two people(if people is same, then indicate one person) from here or there besides `light`
    """
    here, there = state
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
                        successors[(here - tmp_fronzenset, there | tmp_fronzenset)] = ['%s, %s, light ->' % (a, b), t + max(a, b)]
    else:
        for a in there:
            if a is not 'light':
                for b in there:
                    if b is not 'light':
                        tmp_fronzenset = frozenset([a, b, 'light'])
                        successors[(here | tmp_fronzenset, there - tmp_fronzenset)] = ['%s, %s, light <-' % (a, b), t + max(a, b)]

    return successors


def final_state(path):
    return path[-1]


def add_path_to_frontier(frontier, path):
    """Add path to frontier, replacing costlier path if there is one"""
    old = None
    # two different paths end in the same state, so we want to remove the
    # costlier path
    for i, p in enumerate(frontier):
        if final_state(p) == final_state(path):
            old = i
            break
    if old is not None:
        if path_cost(frontier[old]) > path_cost(path):
            del frontier[old]  # old path is worse, so delete it
            # -------------------add current path, and resort-------------------
            frontier.append(path)
            frontier.sort(key=path_cost)
            return frontier
            # -------------------add current path, and resort-------------------
        else:
            # old path is better, so don't append current path, just return
            return frontier
    else:
        # -------------------add current path, and resort-------------------
        frontier.append(path)
        frontier.sort(key=path_cost)
        return frontier
        # -------------------add current path, and resort-------------------


def bridge_problem(here):
    """

    :param here: a individual list represented minutes to pass the bridge
    :return:
    """
    # initialize, the `light` is in `here`
    here = frozenset(here) | frozenset(['light'])
    frontier = [ [(here, frozenset())], ]
    explored = set()

    while frontier:
        path = frontier.pop(0)
        t = path_cost(path)
        here, there, = state1 = final_state(path)
        if not here or (len(here) == 1 and 'light' in here):
            return path
        # TODO why this code move to `for` loop below will take more minutes?
        explored.add(state1)
        for state, action in bsuccessors(state1, t).items():
            if state not in explored:
                # explored.add(state)
                path2 = path + [action, state]
                add_path_to_frontier(frontier, path2)


result = bridge_problem([1, 2, 5, 10])
print(result[-2])
print(result)
# print(bsuccessors( ( frozenset([1, 2, 3, 'light'],), frozenset()), 0))
