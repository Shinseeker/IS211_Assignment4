#!user/bin/env python
# -*- coding: utf-8 -*-
"""IS211 Assignment Week 4"""


import time
import random


def insertion_sort(a_list):
    start = time.time()
    """Insertion list sort function."""
    for index in range(1, len(a_list)):
        current_value = a_list[index]
        position = index
        while position > 0 and a_list[position - 1] > current_value:
            a_list[position] = a_list[position - 1]
            position = position - 1
        a_list[position] = current_value
    end = time.time()
    elapsed = end - start
    return a_list, elapsed

def shell_sort(a_list):
    start = time.time()
    """A shell list sort function."""
    sublist_count = len(a_list) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(a_list, start_position, sublist_count)
        sublist_count = sublist_count // 2
    end = time.time()
    elapsed = end - start
    return a_list, elapsed

def gap_insertion_sort(alist, start, gap):
    """ Implementation of gap insertion sort"""
    for x in range(start + gap, len(alist), gap):
        current_value = alist[x]
        position = x
        while position >= gap and alist[position - gap] > current_value:
            alist[position] = alist[position - gap]
            position = position - gap
            alist[position] = current_value

def python_sort(a_list):
    start = time.time()
    """A list sort function."""
    a_list = a_list.sort()
    end = time.time()
    elapsed = end - start
    return a_list, elapsed


def main():
    """The main function of the program."""

    """ Insertion Sort """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        found, time = insertion_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        found, time = insertion_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        found, time = insertion_sort(random_list)
        total_time += time
    
    print "Insertion Sort took %10.7f seconds to run, on average" % (total_time / 300)

    """ Shell Sort """

    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        found, time = shell_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        found, time = shell_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        found, time = shell_sort(random_list)
        total_time += time
    print "Shell Sort took %10.7f seconds to run, on average" % (total_time / 300)

    """ Python Sort """
 
    total_time = 0

    """ Generate 100 random lists of size 500 """
    for x in range(0, 100):
        random_list = random.sample(xrange(500), 500)
        found, time = python_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 1000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(1000), 1000)
        found, time = python_sort(random_list)
        total_time += time
    """ Generate 100 random lists of size 10000 """
    for x in range(0, 100):
        random_list = random.sample(xrange(10000), 10000)
        found, time = python_sort(random_list)
        total_time += time
    print "Python Sort took %10.7f seconds to run, on average" % (total_time / 300)
   
if __name__ == "__main__":
    main()
