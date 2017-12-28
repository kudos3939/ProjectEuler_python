#!/usr/bin/python
# coding: utf-8
from util import find_primes


# 10001番目の素数を求めます。
def q7():
    length = 0  # 帰ってきた素数リストの長さを格納するための変数です。
    a_number = 10000  # まず最初は10000までの素数を求めます。
    while length < 10001:  # リストの長さが10001以上になったらループを抜けます。
        prime_numbers = find_primes(a_number)
        length = len(prime_numbers)
        a_number += a_number  # 次のループに備えて数を2倍にします。

    print prime_numbers[10000]  # 先頭は0なので10000の要素をプリントします。


q7()
