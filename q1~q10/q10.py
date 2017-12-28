#!/usr/bin/python
# coding: utf-8
from util import find_primes


# 200万以下の素数を全て足した合計を出します。
def q10():
    prime_numbers = find_primes(2000000)

    # reduce関数に隣り合ったリストの要素を足し合わせるラムダ式と素数のリストを渡します。
    print reduce(lambda a, b: a + b, prime_numbers)


q10()
