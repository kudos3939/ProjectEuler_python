# coding: utf-8
# よく使う関数をモジュールとしてまとめています。
from math import sqrt
from collections import deque


# 素数の可能性が高い数字だけに絞り込みリストにします。
def create_wheel(maximum):
    primes = [2, 3, 5]  # 一つのサイクルは30です。
    step = [6, 4, 2, 4, 2, 4, 6, 2]  # 一つのサイクル内で素数が出現する可能性のあるステップ

    wheel = []  # 素数だと思われる数字を書くのするリスト
    a_number = 1
    while a_number < maximum:
        for n in step:
            a_number += n
            if a_number > maximum:
                break
            wheel.append(a_number)
    return primes + wheel  # 求めたリストと最初の素数リストを足して返します。


# 求めたwheel(素数の可能性が高い数字群)をSieve of Eratosthenesを用いて絞り込みます。
def sieve_prime(wheel):
    prime_numbers = []
    wheel = deque(wheel)
    while wheel[0] < sqrt(wheel[-1]):
        head = wheel.popleft()
        # filter関数でラムダ式に該当する要素だけを抽出します。
        wheel = deque(filter(lambda p: p % head != 0, wheel))
        prime_numbers.append(head)
    prime_numbers += list(wheel)

    return prime_numbers


# wheel factorisation を用いて素数を求めます。
def find_primes(maximum):
    wheel = create_wheel(maximum)
    return sieve_prime(wheel)
