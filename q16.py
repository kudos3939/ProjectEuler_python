#!/usr/bin/python
# coding: utf-8


def q16():
    print reduce(str_sum, list(str(pow(2, 1000))))


def str_sum(first, second):
    result = int(first) + int(second)
    result = str(result)
    return result


q16()
