#!/usr/bin/python
# coding: utf-8


# 二つの3桁の数字を掛け合わせてできる最も大きな回文数を求めます。
def q4():
    palindrome = 0  # 回文数を格納する変数です。

    # ここではforループの中にforループを入れる（ネストする）ことで
    # 100から999までの数字を一つ一つ順番にかけあわせています。（九九をイメージするとわかりやすい）
    for first in range(100, 1000):
        for second in range(100, 1000):
            a_number = first * second  # a_numberは一時変数です（tempと同じ）。
            # 回文数であるかどうか判定する関数に二つの数をかけ合わせた結果をわたし
            # 回文数であった場合、現在格納されている回文数よりも大きいかどうか比べています。
            if is_palindrome(a_number) and a_number > palindrome:
                palindrome = a_number  # 大きければ回文数を更新します。
    print palindrome


# 引数に渡された値が回文数ならTrueを返す関数です。
def is_palindrome(a_number):
    num_str = str(a_number)  # 渡された数字を文字列に変換しています。
    reversed_num = num_str[::-1]  # 文字列の順番を入れ替えています。説明は一番下で。
    # ひっくり返した数と、元の数が同じなら回文数なのでTrueを返します。
    return num_str == reversed_num


q4()

"""
文字列は「文字の配列」なので [] <- この配列の要素を操作する記号が使えます。
基本的な使い方は[]内に数字を入れることでインデックスを指定するのですが

>>> test = "abcde"
>>> test[0]
'a'

負の値を指定することで後ろから配列を遡ることができます。
>>> test[-1]
'e'

そして、[start:end:slice]の構文を使うことで
配列の要素を複数取り出すことができます。
start の位置から順番に配列を end の位置の一個手前まで取り出します。
(数を指定しないとstartは配列の最初、endは配列の最後になります)
sliceを指定しない場合、二個目のコロンは省略できます。

>>> test[1:3:]
'bc'

>>> test[:2:]
'ab'

>>> test[1::]
'bcde'

>>> test[1:3]
'bc'

slice を1以外の数にすることによって、その数ごとに要素を取り出せます。

>>> test[1::2]
'bd'

そして[::-1]と指定すると
配列を進む向きが逆向きになり、startに配列の最後、endに配列の最初が自動的に指定されます。
>>> test[::-1]
'edcba'


"""
