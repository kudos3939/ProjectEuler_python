#!/usr/bin/python
# coding: utf-8


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
    prime_numbers = []
    for x in range(2, max_number):
        temp_array = [x % p for p in prime_numbers]
        if 0 not in temp_array:
            prime_numbers.append(x)
    return prime_numbers


q5()
