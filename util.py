# coding: utf-8
# よく使う関数をモジュールとしてまとめています。


def is_divisible(num, *num_list):
    for n in num_list:
        if num % n == 0:
            return True
    return False
