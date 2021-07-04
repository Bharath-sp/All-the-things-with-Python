# -*- coding: utf-8 -*-
"""
Created on Sat Jul  3 20:14:06 2021
"""

def findpos(l,v):
    """Returns first position of a value v in a given list l
       Returns -1 if v is not in l"""
    for i in range(len(l)):
        if l[i]==v:  # Exit, report position
            pos = i
            break
    else:
        pos = -1  #no break, v not in l
    return(pos)  #pos will be 0 to (n-1) or -1
    
"""
else clause of loop has been used here.
Another way to do this is:

def findpos(l,v):
    pos = -1
    for i in range(len(l)):
        if l[i]==v:   
            pos = i
            break
    return(pos)  #if pos not reset in loop, pos is -1
"""


