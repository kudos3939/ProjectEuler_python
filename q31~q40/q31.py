#!/usr/local/bin/python3
COINS = {'a': 1, 'b': 2, 'c': 5, 'd': 10,
         'e': 20, 'f': 50, 'g': 100, 'h': 200}


def q31():

    pool = set()
    combination(10, pool=pool)
    print(pool)


def combination(limit, total=0, pool=set(), c_array=[], cache={}):
    if total is limit:
        comb = ''.join(sorted(c_array))
        if comb not in pool:
            pool.add(comb)
    elif total < limit:
        for c in sorted(COINS.keys()):
            new_total = total + COINS[c]
            new_array = c_array+[c]
            if new_total in cache.keys():
                cache[new_total].add(tuple(sorted(new_array)))
            else:
                cache[new_total] = set(tuple(sorted(new_array)))
            combination(limit, new_total, pool, new_array, cache)


q31()
