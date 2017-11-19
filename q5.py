#!/usr/bin/python
# coding: utf-8
from util import is_divisible  # モジュールをインポートします。
"""
※ 実際にコードを試してみたい方はq5.pyとutil.pyを同じディレクトリに配置してください。
"""


# 1から20全ての数字の最小公倍数を求めます。
def q5():
    smallest_multiple = 1
    prime_numbers = find_primes(20)

    # それぞれの素数を順番に処理しています。
    for p in prime_numbers:
        biggest_power = p  # その素数の最も大きい累乗(ただし20以下)を求めます。
        while biggest_power * p < 20:
            biggest_power *= p
        smallest_multiple *= biggest_power  # 最小公倍数の変数にかけ合わせます。
    smallest_multiple = 1
    print smallest_multiple


# 与えられた引数までの素数を求め、配列を返します。
def find_primes(max_number):
    prime_numbers = [2]  # 空だとis_divisibleを呼び出した時エラーになるので2を予め入れています。
    for x in range(3, max_number):  # 0からだと0と1も入ってしまい、2がダブります。
        if is_divisible(x, prime_numbers):  # importした関数を呼び出しています。
            prime_numbers.append(x)
    return prime_numbers


q5()
