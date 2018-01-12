#!/usr/bin/python
# coding: utf-8
import datetime


def q19():
    count = 0
    year = 1901
    month = 1

    while year < 2001:
        if month == 12:
            year += 1
            month = 1
        else:
            month += 1

        date = datetime.date(year, month, 1)
        if date.weekday() is 6:
            count += 1

    print count


q19()
