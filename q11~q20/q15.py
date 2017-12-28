#!/usr/bin/python
# coding: utf-8
known_path = {}


def q15():
    print next_path(0, 0)


def next_path(x, y):
    num_grid = 20
    counter = 0
    if (x, y) in known_path:
        return known_path[(x, y)]
    if x == num_grid or y == num_grid:
        return 1
    counter += next_path(x + 1, y)
    counter += next_path(x, y + 1)

    known_path[(x, y)] = counter

    return counter


q15()
