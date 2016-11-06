# -*- coding: utf-8 -*-
import re

import itertools

__author__ = 'Simon'

"""https://en.wikipedia.org/wiki/Verbal_arithmetic"""


def compile_formula(formula, verbose=False):
    """Given formula into a function. Also return letters found, as a str,
    in same order as params of function. For example 'YOU == ME**2' returns
    (lambda Y, O, U, M, E: (U+10*O+100*Y) == (E+10*M)**2), 'YOUME' """
    letters = ''.join(set(re.findall('[A-Z]', formula)))
    params = ', '.join(letters)
    tokens = map(compile_word, re.split('([A-Z]+)', formula))
    body = "".join(tokens)
    f = 'lambda %s: %s' % (params, body)
    if verbose: print(f)
    return eval(f), letters


def faster_solve(formula):
    """Given a formula like 'ODD + ODD == EVEN', fill in digits to solve it.
    Input formula is a string; output is a digit-filled-in string or None.
    This version precompiles the formula; only one eval per formula"""
    f, letters = compile_formula(formula)
    for digits in itertools.permutations(range(10), len(letters)):
        try:
            if f(*digits) is True:
                table = str.maketrans(letters, ''.join(map(str, digits)))
                return formula.translate(table)
        except ZeroDivisionError as e:
            pass


def compile_word(word):
    """Compile a word of uppercase letters as numeric digits.
    E.g., compile_word('YOU') => '(1*U+10*O+100*Y)'
    Non-uppercase words unchanged: compile_word('+')=>'+' """
    if not word.isupper():
        return word
    else:
        terms = ['%s*%s' % (10**i, d)
                 for (i, d) in enumerate(word[::-1])]
        return '(' + '+'.join(terms) + ')'
