#!/usr/bin/python
# coding: utf-8


def q22():
    total = 0

    f = open('q022_names.txt', 'r')
    names = f.readline().split(',')
    names = [name.strip('\"') for name in names]
    names.sort()

    for i in range(len(names)):
        total += cal_score(names[i], i+1)

    print total


def cal_score(name, rank):
    score = 0
    pos = "0ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    for char in name:
        score += pos.index(char)
    score *= rank

    return score

q22()
