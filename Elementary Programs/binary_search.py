# -*- coding: utf-8 -*-
"""
Created on Sun Jul  4 22:21:48 2021
"""
def bsearch(v, list, l, r):
    """ Returns True if the provided value was present in the given SORTED list
        Pass (value, list, 0, len(list))"""
    if (r-l==0):
        return(False)
    mid = (r+l)//2
    if v == list[mid]:   #case 1
        return(True)
    if v < list[mid]:    #case 2
        return(bsearch(v,list,l,mid))
    else:   #case 3
        return(bsearch(v,list,mid+1,r))

