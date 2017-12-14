#!/usr/bin/python
# coding: utf-8
from collections import deque


def q18():
    f = open('q18_number', 'r')
    # 数字をノード化しデックに納めます。
    num_of_line = 0
    nodes = []
    for line in f.readlines():
        line = [Node(num) for num in line.split()]
        nodes.append(line)
        num_of_line += 1

    for i in range(num_of_line):
        for j in range(i):
            nodes[j]


class Node:
    __value = 0
    __path = None
    __total_value = 0

    def __init__(self, value):
        self.__value = value

    def __lt__(self, other):
        return self.__total_value < other.get_value()

    def retrieve_path(self):
        return 0

    def get_value(self):
        return self.__total_value

    def __repr__(self):
        return str(self.__value)

q18()
