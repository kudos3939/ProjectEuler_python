#!/usr/bin/python
# coding: utf-8
from util import is_divisible


# 10001番目の素数を求めます。
def q7():

    prime_numbers = [2]  # 最小の素数を予め入れとく
    counter = 1  # 何番目の素数か数えてくれます。2がもう入っているので1から始まります。
    n_number = 2  # 試される数です。ループの最初でインクリメントするので2からになります。(最初に試される数は3）
    while counter < 10001:  # カウンターが10001になったらループを抜けます。
        n_number += 1
        if not is_divisible(n_number, *prime_numbers):
            prime_numbers.append(n_number)
            counter += 1
    print n_number


q7()
