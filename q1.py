#!/usr/bin/python
# coding: UTF-8


# 1000未満の全ての3の倍数と5の倍数の合計を出力します。
def q1():
    maximum = 1000  # 最大値
    result = 0  # 結果を格納するための変数
    # 0から999まで順番にxに代入していきます。
    for x in range(0, maximum):
        # xが3の倍数、または5の倍数であるかチェックします。
        if x % 3 == 0 or x % 5 == 0:
            result += x  # チェックがTrueを返したら変数に加えます。

    print result  # コンソールへ出力します。


# q1を呼び出しています。プログラムはここから始まります。
q1()
