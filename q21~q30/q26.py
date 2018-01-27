#!/usr/local/bin
import util


def q26(num, divisor):
    seq_digits = ''
    remainders = set()
    sub_remainders = set()
    cycle_length = 0
    remainder = num
    while remainder > 0:
        quot = 0
        for n in range(0, 10):
            test2 = remainder - divisor * n
            if test2 < 0:
                break
            if test2 >= divisor:
                continue
            quot = n
            remainder = test2

        if cycle_length or str(quot) in seq_digits:
            sub_remainders.add(remainder)

        seq_digits += str(quot)
        remainders.add(remainder)
        intersection = len(remainders & sub_remainders)
        if intersection > cycle_length:
            cycle_length = intersection
        elif cycle_length != 0:
            break
        remainder *= 10

    return cycle_length


primes = util.find_primes(1000)
longest = (0, 0)
for x in primes:
    temp3 = q26(1, x)
    if temp3 > longest[1]:
        longest = x, temp3

print(longest)
