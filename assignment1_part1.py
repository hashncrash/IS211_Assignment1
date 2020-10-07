##!/usr/bin/env python
# -*- coding: utf-8 -*-
"IS 211 Assignment 1, part 1.  Dave Soto"


def listDivide(numbers, divide=2):
    "function called testListDivide that performs the following tests on listDivide"

    divcount = 0
    for item in numbers:
        if item % divide is 0:
            divcount += 1
    return divcount


class ListDivideException(Exception):
    "Custom Exception"
    pass


def testListDivide():
    "A function to test ListDivide."
    if listDivide([1, 2, 3, 4, 5]) != 2:
        raise ListDivideException
    elif listDivide([2, 4, 6, 8, 10]) != 5:
        raise ListDivideException
    elif listDivide([30, 54, 63, 98, 100], 10) != 2:
        raise ListDivideException
    elif listDivide([]) != 0:
        raise ListDivideException
    elif listDivide([1, 2, 3, 4, 5], 1) != 5:
        raise ListDivideException

if __name__ == "__main__":
    testListDivide()
