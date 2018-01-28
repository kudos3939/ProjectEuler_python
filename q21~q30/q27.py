#!/usr/bin/python
import util


def q27(an, bn):
    count = 0
    for n in range(10000):
        p = n ** 2 + n * an + bn
        if p not in primes:
            break
        count += 1
    return count


length = 0
longest = 0
nums = ()
primes = util.find_primes(100000)
primes = [1] + primes
tested = [x for x in primes if x <= 1000]
tested += [-x for x in tested]
for a in tested:
    for b in tested:
        length = q27(a, b)
        if length > longest:
            longest = length
            nums = (a, b)

print(nums, longest)
print(nums[0]*nums[1])
