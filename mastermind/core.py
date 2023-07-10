#! -*- coding: utf-8 -*-
"""
Mastermid core functions
"""
import random
import itertools

import pytest


def generate_combination(params):
    product = list(itertools.product(range(params.irange), repeat=params.clenght))
    idx = random.randint(0, len(product))
    return ''.join(map(str, product[idx]))


def response(combination, guess):
    resp = ""

    cg = list(zip(combination, guess))
    for c, g in cg[:]:
        if c == g:
            resp += 'x'
            cg.remove((c, g))

    c_remain = [i[0] for i in cg]
    g_remain = [i[1] for i in cg]

    match = 0

    for g in g_remain:
        if g in c_remain:
            c_remain.remove(g)
            match += 1

    resp += 'o' * match

    return resp


@pytest.mark.parametrize('combination, guess, resp', [
    ('5022', '5022', 'xxxx'),
    ('5022', '1111', ''),
    ('5022', '2205', 'oooo'),
    ('5022', '1234', 'o'),
    ('0144', '1212', 'o'),
    ('0111', '0000', 'x'),
])
def test_response(combination, guess, resp):
    assert resp == response(combination, guess)


def is_guess_ok(guess, clenght, irange):
    if len(guess) != clenght:
        return False

    # Each item in guess combination can't be greater than
    # the given irange patameter
    for i in guess:
        if int(i) >= irange:
            return False
    return True


@pytest.mark.parametrize('guess, clenght, irange, expected', [
    ('1234', 4, 6, True),
    ('0000', 4, 6, True),
    ('0005', 4, 6, True),
    ('0006', 4, 6, False),
    ('0007', 4, 6, False),
    ('00000', 4, 6, False),
])
def test_is_guess_ok(guess, clenght, irange, expected):
    assert is_guess_ok(guess, clenght, irange) == expected
