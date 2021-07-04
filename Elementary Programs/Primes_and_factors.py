# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:41:41 2021
"""
def factors(n):
    """Returns factors of n. Factors of n are numbers between 1 to n that divide n"""
    fact_list=[]
    for i in range(1,n+1):
        if n%i == 0:
            fact_list = fact_list+ [i]
    return(fact_list)

def isprime(n):
    """ Returns True if n is prime. Prime number - Only factors are 1 and itself. 1 is not a prime number"""
    return(factors(n)==[1,n])
    
def primesupto(n):
    """ Returns a list with prime numbers up to n"""
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist=primelist+[i]
    return(primelist)
    
def nprimes(n):
    """ Returns a list with first n prime numbers"""
    (count, i, plist)=(0,1,[])
    while count < n:
        if isprime(i):
            (count, plist)=(count+1, plist+[i])
        i=i+1
    return(plist)

"""
primesupto(): know we have to scan from 1 to n, use for
nprimes(): Range to scan is not known in advance, use while
"""
