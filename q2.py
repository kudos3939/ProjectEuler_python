#!/usr/bin/python
# coding: utf-8


# フィボナッチ数列から得られた400万以下の数で偶数であるものの合計を出力します。
def q2():
    total = 2  # 合計を格納する変数。以下のループで処理されない2をあらかじめ入れてあります。
    first = 1  # 一つ目の数字を格納する変数。最初は1
    second = 2  # 二つ目の数字を格納する変数。最初は2
    # firstとsecondの合計が400万未満であるかぎり以下の処理を続けます。
    while (first + second) < 4000000:
        temp = first + second  # 合計を一時変数(temp)に代入します。
        # 二つの数の合計が偶数であればtotalに加えます。
        if temp % 2 == 0:
            total += temp
        first = second  # secondに格納された値をfirstの変数に代入します。
        second = temp  # tempに格納していた数字をsecondに代入します。

    print total


q2()
