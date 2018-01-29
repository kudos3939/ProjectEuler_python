#!/usr/local/bin/python3


def q30():
    digit_powers = []
    for n in range(2, 1000000):
        total = 0
        string = str(n)
        for s in string:
            total += int(s)**5
        diff = n - total
        if diff is 0:
            digit_powers.append(n)
    print(sum(digit_powers))


q30()
