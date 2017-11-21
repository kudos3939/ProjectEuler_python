#!/usr/bin/python
# coding: utf-8


# a^2 + b^2 = c^2, a + b + c = 1000, a < b < c が共に成り立つ積abcを求めます。
def q9():
    for a in range(1000):
        for b in range(1000):
            if b <= a:
                continue  # 条件をみたさないので以下を処理せず次のループへいきます。
            c = 1000 - (a + b)
            if c <= 0:  # cが0以下にならないように保証します。
                continue
            if pow(a, 2) + pow(b, 2) == pow(c, 2):
                result = a * b * c

    print result


q9()
