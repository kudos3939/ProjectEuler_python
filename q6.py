#!/usr/bin/python
# coding: utf-8


# 自然数1から100までをそれぞれ二乗したものの合計と、全てを合計を二乗したものの差を求めます。
def q6():
    sum_of_squares = 0  # それぞれの二乗の合計
    square_of_sum = 0  # 全ての合計の二乗

    # 1から100までの自然数の二乗を加えていきます。
    for n in range(1, 101):
        sum_of_squares += n * n

    # 1から100までの自然数を加えていきます。
    for n in range(1, 101):
        square_of_sum += n
    square_of_sum *= square_of_sum  # 二乗します。

    print square_of_sum - sum_of_squares


q6()
