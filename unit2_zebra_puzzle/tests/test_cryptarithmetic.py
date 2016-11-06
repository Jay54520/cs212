# -*- coding: utf-8 -*-
import time

from unit2_zebra_puzzle.cryptarithmetic import solve
from unit2_zebra_puzzle.zebra_puzzle import timedcall

__author__ = 'Simon'

examples = """TWO + TWO == FOUR
A**2 + B**2 == C**2
A**2 + BE**2 == BY**2
X / X == X
A**N + B**N == C**N and N > 1
ATOM**0.5 == A + TO + M
GLITTERS is not GOLD
ONE < TWO and FOUR < FIVE
ONE < TWO < THREE
RAMN == R**3 + RM**3 == N**3 + RX**3
sum(range(AA)) == BB
sum(range(POP)) == BOBO
ODD + ODD == EVEN
PLUTO not in set([PLANTS])
""".splitlines()


def test():
    t0 = time.clock()
    for example in examples:
        print(13 * ' ', example)
        result = timedcall(solve, example)
        print('%6.4f sec: %s ' % (result[1], result[0]))
    print('%6.4f tot.' % (time.clock() - t0))
