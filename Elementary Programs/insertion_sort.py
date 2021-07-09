# -*- coding: utf-8 -*-
"""
Created on Thu Jul  8 01:37:14 2021
"""

def InsertionSort(seq):
    """ Returns None. Provided list is sorted in place"""
    for pos in range(len(seq)):
        while pos>0 and seq[pos]<seq[pos-1]:
            (seq[pos], seq[pos-1])=(seq[pos-1], seq[pos])
            pos=pos-1
            
def InsertionSortRec(seq):
    """ Returns None. Provided list is sorted recursively in place"""
    isort(seq,len(seq))
    
def isort(seq,k):
    if k>1:
        isort(seq,k-1)
        insert(seq,k-1)
        
def insert(seq,k):
    pos = k
    while pos>0 and seq[pos]<seq[pos-1]:
        (seq[pos], seq[pos-1])=(seq[pos-1], seq[pos])
        pos=pos-1
        
    