#!/usr/bin/python
# coding: utf-8
from collections import deque


def q18():
    f = open('q18_number', 'r')
    # 数字をノード化しデックに納めます。
    num_of_line = 0
    nodes = []
    the_sum = 0
    for line in f.readlines():
        line = [Node(int(num)) for num in line.split()]
        nodes.append(line)
        num_of_line += 1

    for n in range(num_of_line - 1):
        for j in range(len(nodes[n])):
            nodes[n+1][j].set_value(nodes[n][j])
            nodes[n+1][j+1].set_value(nodes[n][j])

    for n in nodes[num_of_line - 1]:
        if the_sum < n.get_value():
            the_sum = n.get_value()

    print the_sum


class Node:
    def __init__(self, value):
        self.__value = value
        self.__total_value = value
        self.__path = None

    def get_value(self):
        return self.__total_value

    def set_value(self, node):
        if self.__total_value < node.get_value() + self.__value:
            self.__total_value = node.get_value() + self.__value
            self.__path = node

    def __repr__(self):
        return str(self.__value)


q18()
