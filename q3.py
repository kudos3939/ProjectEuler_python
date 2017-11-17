#!/usr/bin/python


def q3():
    the_number = 600851475143
    largest_prime = 2
    i = 0

    while the_number != 1:
        i += 1
        if (the_number % i) == 0:
            largest_prime = i
            the_number /= i
    print largest_prime


q3()
