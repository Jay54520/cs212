# -*- coding: utf-8 -*-
import re

import itertools

__author__ = 'Simon'

"""https://en.wikipedia.org/wiki/Verbal_arithmetic"""


def fill_in(formula):
    """return generator of eval string mapped from formula """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    if len(letters) > 10:
        raise TypeError("unique letters in formula are greater than 10")

    for digits in itertools.permutations(range(10), len(letters)):
        table = str.maketrans(letters, ''.join("%s" % digit for digit in digits))
        # use yield because you may be lucky finding the answer at first,
        # then you don't need to calculate the rest of the list
        yield formula.translate(table)


def solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None."""
    fs = fill_in(formula)
    for f in fs:
        if valid(f):
            return f

    return None


def valid(f):
    """Formula f is valid if it has not numbers with leading zero, and evals true."""
    try:
        return not re.search(r'\b0[0-9]', f) and eval(f) is True
    except ZeroDivisionError as e:
        return False
