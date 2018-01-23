#!/usr/bin/python
# coding: utf-8


def q24():
    numbers = range(10)
    str_numbers = [str(n) for n in numbers]
    perms = []
    find_perms(str_numbers, '', perms)

    print(perms[999999])


def find_perms(nums, digits, perms=[]):
    if len(nums) is 0:
        perms.append(digits)
    for x in nums:
        new_nums = [r for r in nums if r != x in nums]
        find_perms(new_nums, digits + x, perms)


q24()
