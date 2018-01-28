#!/usr/local/bin/python3


def q29():
    pool = set()
    for a in range(2, 101):
        for b in range(2, 101):
            pool.add(a ** b)

    print(len(pool))


q29()
