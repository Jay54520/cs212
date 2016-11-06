# -*- coding: utf-8 -*-

__author__ = 'Simon'

def test_search():
    a, b, c = lit('a'), lit('b'), lit('c')
    abcstars = seq(star(a), seq(star(b)), seq(start(c)))
    dotstar = star(dot)
    assert search(lit('def'), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdef') == 'def'
    assert search(seq(lit('def'), eol), 'abcdefg') == None
    assert search(a, 'not the start') == a
    assert match(a, 'not the start') == None
    assert match(abcstars, 'aaabbbccccccdef') == 'aaabbbcccccc'
    assert match(abcstars, 'junk') == ''
    assert all(match(seq(abcstars, eol), s) == s
               for s in 'abc aaabbccd abccccc'.split())
    assert all(match(seq(abcstars, eol), s) == None
               for s in 'abc aaabbccd aaaa-b-cccc'.split())
    r = seq(lit('ab'), seq(dotstar, seq(lit('aca'), seq(dotstar, seq(a, eol)))))
    assert all(search(r, s) is not None
               for s in 'ababab abacaa about-acaca-flora'.split())


