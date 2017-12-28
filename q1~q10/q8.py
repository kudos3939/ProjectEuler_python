#!/usr/bin/python
# coding: utf-8


# 1000桁の数字(q8_number)からそれぞれの桁をかけた数が最大になる13桁を求めます。
def q8():
    f = open("q8_number", 'r')  # q8_numberのファイルを読み込むオブジェクトを作ります。
    the_number = f.read()  # q8_numberを変数に代入します(型はstrです)。
    biggest_number = 0

    # xは最初の桁のインデックスを示しています。
    for x in range(len(the_number)):
        # 変数からx番目〜x+4番目の数字(str)を取り出し
        # それぞれの桁にint()関数を適用してint型にして一つづつ配列に収めています。
        a_number = [int(i) for i in the_number[x:x + 13]]
        # reduceを用いて一桁ずつ収められた配列内の数字を全て掛け合わせています。
        a_number = reduce(lambda a, b: a * b, a_number)
        if a_number > biggest_number:
            biggest_number = a_number

    print biggest_number


q8()
