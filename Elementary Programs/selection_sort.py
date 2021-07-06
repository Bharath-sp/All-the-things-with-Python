# -*- coding: utf-8 -*-
"""
Created on Tue Jul  6 21:26:20 2021
"""

def SelectionSort(l):
    """Returns None. Provided list is sorted in place"""
    for start in range(len(l)):
        minpos = start
        for i in range(start+1, len(l)):
            if l[i]<l[minpos]:
                minpos = i
        (l[start], l[minpos])=(l[minpos], l[start])
            