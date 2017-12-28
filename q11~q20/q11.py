#!/usr/bin/python
# coding: utf-8


# q11_numberの20*20の行列から縦横斜めで隣り合う4つの数字の積が最も大きくなる組み合わせを求めます。
def q11():
    matrix = []
    f = open('q11_number', 'r')
    for line in f.readlines():
        matrix.append(line.split())  # 一つの行をスペースで区切ってそれぞれ配列に入れています。
    # リストのリストなので、mapを二重にしています。
    matrix = [[int(n) for n in l] for l in matrix]

    biggest_number = 0

    # 縦の組み合わせを探すループ
    for y in range(20):
        for x in range(17):  # x(0~16) + 4 = 4~20
            a_number = reduce(lambda a, b: a * b, matrix[y][x:x + 4])  # matrixのy行目のxからx+4番目の配列を掛け合わせます。
            if a_number > biggest_number:
                biggest_number = a_number

    # 横の組み合わせを探すループ
    for x in range(20):
        for y in range(17):  # y(0~16) + i(0~3) = 0~19
            a_number = 1  # リセットします。そうしないと数字がそのまま引き継がれてめんどくさいことに。
            for i in range(4):
                a_number *= matrix[y+i][x]
                if a_number > biggest_number:
                    biggest_number = a_number

    # \斜め\の組み合わせを探すループ
    for x in range(17):
        for y in range(17):
            a_number = 1
            for i in range(4):
                a_number *= matrix[y+i][x+i]
                if a_number > biggest_number:
                    biggest_number = a_number

    # /斜め/の組み合わせを探すループ
    for x in range(19, 2, -1):
        for y in range(17):
            a_number = 1
            for i in range(4):
                a_number *= matrix[y+i][x-i]
                if a_number > biggest_number:
                    biggest_number = a_number

    print biggest_number


q11()
