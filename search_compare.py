#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""

import random
import time


def sequential_search(alist, item):
    start = time.time()
    pos = 0
    found = False

    while pos < len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos = pos + 1
    end = time.time()
    elapsed = end - start
    return found, elapsed


def ordered_sequential_search(alist, item):
    start = time.time()
    pos = 0
    found = False
    stop = False

    while pos < len(alist) and not found and not stop:
        if alist[pos] == item:
            found = True
        else:
            if alist[pos] > item:
                stop = True
            else:
                pos = pos + 1
    end = time.time()
    elapsed = end - start
    return found, elapsed


def binary_search_iterative(alist, item):
    start = time.time()
    first = 0
    last = len(alist) - 1
    found = False

    while first <= last and not found:
        midpoint = (first + last) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                last = midpoint - 1
            else:
                first = midpoint + 1
    end = time.time()
    elapsed = end - start
    return found, elapsed


def binary_search_recursive(alist, item):
    start = time.time() 
    if len(alist) == 0:
        found = False
    else:
        midpoint = len(alist) // 2
        if alist[midpoint] == item:
            found = True
        else:
            if item < alist[midpoint]:
                return binary_search_recursive(alist[:midpoint], item)
            else:
                return binary_search_recursive(alist[midpoint + 1:], item)
    end = time.time()
    elapsed = end - start
    return found, elapsed


def main():
    """The program itself"""

    """ Sequential Search """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        found, time = sequential_search(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        found, time = sequential_search(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        found, time = sequential_search(random_list, -1)
        total_time += time
    print "Sequential Search took %10.7f seconds to run, on average" % (total_time / 300)
   
    """ Ordered Sequential Search """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        random_list.sort()
        found, time = ordered_sequential_search(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        random_list.sort()
        found, time = ordered_sequential_search(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        random_list.sort()
        found, time = ordered_sequential_search(random_list, -1)
        total_time += time
    print "Ordred Sequential Search took %10.7f seconds to run, on average" % (total_time / 300)

    """ Binary Search Iterative """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        random_list.sort()
        found, time = binary_search_iterative(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        random_list.sort()
        found, time = binary_search_iterative(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        random_list.sort()
        found, time = binary_search_iterative(random_list, -1)
        total_time += time
    print "Iterative Binary Search took %10.7f seconds to run, on average" % (total_time / 300)

    """ Binary Search Recursive """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        random_list.sort()
        found, time = binary_search_recursive(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        random_list.sort()
        found, time = binary_search_recursive(random_list, -1)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        random_list.sort()
        found, time = binary_search_recursive(random_list, -1)
        total_time += time
    print "Recursive Binary Search took %10.7f seconds to run, on average" % (total_time / 300)

if __name__ == '__main__':
    main()
