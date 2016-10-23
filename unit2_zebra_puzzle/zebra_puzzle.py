# -*- coding: utf-8 -*-
import time
import itertools
__author__ = 'Simon'

"""
The following version of the puzzle appeared in Life International in 1962:

There are five houses.
The Englishman lives in the red house.
The Spaniard owns the dog.
Coffee is drunk in the green house.
The Ukrainian drinks tea.
The green house is immediately to the right of the ivory house.
The Old Gold smoker owns snails.
Kools are smoked in the yellow house.
Milk is drunk in the middle house.
The Norwegian lives in the first house.
The man who smokes Chesterfields lives in the house next to the man with the fox.
Kools are smoked in the house next to the house where the horse is kept.
The Lucky Strike smoker drinks orange juice.
The Japanese smokes Parliaments.
The Norwegian lives next to the blue house.
Now, who drinks water? Who owns the zebra?

In the interest of clarity, it must be added that each of the five houses is painted a different color, and
their inhabitants are of different national extractions, own different pets, drink different beverages and
smoke different brands of American cigarets [sic]. One other thing: in statement 6, right means your right.

— Life International, December 17, 1962

`Analysis`:
    All possibilities:
        (5!)^5 is about 2.5 billion
    Assignment:
        * house[1].add('red)    set()
        * house[1].color = 'red'    House() :type: class
        * red = 1
"""


def imright(h1, h2):
    """House h1 is imediately right of h2 if h1-h2 == 1"""
    return h1 - h2 == 1


def next_to(h1, h2):
    """Two houses are next to each other if they differ by 1"""
    return abs(h1-h2) == 1


def c(sequence):
    """Generate items in sequence; keeping counts as we go. c.starts is the
    number of sequences started; c.items is number of items generated."""
    c.starts += 1
    for item in sequence:
        c.items += 1
        yield item


def zebra_puzzle():
    """Return a tuple (WATER, ZEBRRA) indicating their house numbers"""
    houses = first, _, middle, _, _ = [1, 2, 3, 4, 5]
    orderings = list(itertools.permutations(houses))
    return next((WATER, ZEBRA)  # a generator
            for (red, green, ivory, yellow, blue) in c(orderings)
            if imright(green, ivory)
            for (Englishman, Spaniard, Ukrainian, Norwegian, Japanese) in c(orderings)
            if (Englishman is red)
            if (Norwegian is first)
            if next_to(Norwegian, blue)
            for (dog, fox, snails, horse, ZEBRA) in c(orderings)
            if (Spaniard is dog)
            for (coffee, tea, milk, orange_juice, WATER) in c(orderings)
            if (milk is middle)
            if (coffee is green)
            if (Ukrainian is tea)
            for (OldGold, Kools, Chesterfields, LuckyStrike, Parliaments) in c(orderings)
            if (OldGold is snails)
            if (Kools is yellow)
            if next_to(Chesterfields, fox)
            if next_to(Kools, horse)
            if (LuckyStrike, orange_juice)
            if (Japanese, Parliaments)
            )


def func_elapsed_time(func, *args, **kwargs):
    """Call function with args; return the time in seconds and result"""
    t0 = time.clock()
    result = func(*args, **kwargs)
    t1 = time.clock()
    return "The result is {result}, elapsed time is {elapsed_time}".format(
        result=result, elapsed_time=t1-t0
    )


def timedcall(fn, *args, **kwargs):
    """Call fn(*args, **kwargs); return the time in seconds and result"""
    t0 = time.clock()
    result = fn(*args, **kwargs)
    t1 = time.clock()
    return result, t1-t0


def average(numbers):
    """Return the average of a sequence of numbers"""
    return sum(numbers) / float(len(numbers))


def timedcalls(n, fn, *args, **kwargs):
    """Call fn(*args, **kwargs) repeatedly: n times if n is an int, or up to
    n seconds if n is a float; reeturn the min, avg, and max time."""
    if isinstance(n, int):
        times = [timedcall(fn, *args, **kwargs)[1] for _ in range(n)]
    elif isinstance(n, float):
        times= []
        while sum(times) < n:
            times.append(timedcall(fn, *args, **kwargs)[1])
    else:
        raise TypeError("n must be an int or float.")
    return min(times), average(times), max(times)


def all_ints():
    """Generate integers in the order 0, +1, -1, +2, -2, +3, -3, ..."""
    i = 0
    yield i
    while True:
        i += 1
        yield i
        yield -i


def instrument_fn(fn, *args, **kwargs):
    c.starts, c.items = 0, 0  # init the two properties of function `c`
    result = fn(*args, **kwargs)
    print('%s got %s with %5d iters over %7ditems' %(
        fn.__name__, result, c.starts, c.items
    ))


if __name__ == '__main__':
    instrument_fn(zebra_puzzle)
    instrument_fn(timedcalls, 100, zebra_puzzle)