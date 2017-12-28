#!/usr/bin/python
# coding: utf-8
NUMBERS = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven',
           '8': 'eight', '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen',
           '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
TENS = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty',
        '9': 'ninety'}


def q17():
    count = 0
    for n in range(1, 1001):
        count += len(convert_to_eng(n))
    print count


def convert_to_eng(digits):
    if digits < 20:
        return NUMBERS[str(digits)]
    elif digits < 100:
        str_digits = str(digits)
        return TENS[str_digits[0]] + NUMBERS[str_digits[1]]
    elif digits < 1000:
        str_digits = str(digits)
        if digits % 100 == 0:
            return NUMBERS[str_digits[0]] + 'hundred'
        return NUMBERS[str_digits[0]] + 'hundredand' + convert_to_eng(int(str_digits[1:]))
    elif digits == 1000:
        return 'onethousand'


q17()
