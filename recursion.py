#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment14 - Recursion - Tested in Tested in Python 2.7.15"""

def fibonnaci(n):
    if n == 1:
        return 1
    elif n== 1:
        return 1
    elif n == 0:
        return 0
    else:
        return fibonnaci(n-1) + fibonnaci(n-2)

def gcd(a,b):
    while b > 0:
        (a, b) = (b, (a % b))
    return a

def compareTo(s1,s2):
    if len(s1) < len(s2):
        return -1
    elif len(s1) == len(s2):
        return 0
    else:
        len(s1) > len(s2)
        return 1
    return compareTo(s1[1:], s2[1:])

if __name__ == "__main__":
    print "====================================="
    print "The Fibonnaci function of 10 is: %s " % (fibonnaci(10))
    print "======================================"
    print "The GCD function of (50, 75) is: %s " % (gcd(50, 75))
    print "======================================"
    print "The compareTo function s1 < s2 is: %s" % (compareTo("apple", "pineapple"))
    print "======================================"
    print "The compareTo function s1 == s2 is: %s" % (compareTo("pineapple", "pineapple"))
    print "======================================"
    print "The compareTo function s1 > s2 is: %s" % (compareTo("pineapple", "apple"))
    print "======================================"
