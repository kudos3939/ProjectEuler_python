#!/usr/bin/python
# coding: utf-8


# 600851475143の素因数のうち、最も大きなものを出力します。
def q3():
    the_number = 600851475143  # その数字です。
    largest_prime = 2  # 最も大きな素因数が格納されます。最初の値は最も小さい素数です。
    i = 0  # カウンターです。0からループを経るごとに一つづつ大きくなります。

    # 「その数字」が1になる（これ以上割れなくなる）まで繰り返します。
    while the_number != 1:
        i += 1  # 1増やします。
        # iで割ってあまりが0ならば素因数（しかも最も大きい）なので
        if (the_number % i) == 0:
            largest_prime = i  # 記録します。
            the_number /= i  # 「その数字」を素因数でわった数を代入します。
    print largest_prime


q3()
