# -*- coding: utf-8 -*-
"""
Created on Wed Jun 30 21:41:41 2021
Simple python programs
"""
def factors(n):
    """Factors of n are numbers between 1 to n that divide n"""
    fact_list=[]
    for i in range(1,n+1):
        if n%i == 0:
            fact_list = fact_list+ [i]
    return(fact_list)

def isprime(n):
    """ Prime number - Only factors are 1 and itself. 1 is not a prime number"""
    return(factors(n)==[1,n])
    
def primesupto(n):
    primelist=[]
    for i in range(1,n+1):
        if isprime(i):
            primelist=primelist+[i]
    return(primelist)
    
def nprimes(n):
    (count, i, plist)=(0,1,[])
    while count < n:
        if isprime(i):
            (count, plist)=(count+1, plist+[i])
        i=i+1
    return(plist)
            
n=input("Provide a number: ")
result = isprime(int(n))
factor_list=factors(int(n))
primelist = primesupto(int(n))
print("Is {0} a prime number? {1} ".format(n,result))
print("Because the factors of {0} are {1}".format(n,factor_list))
print("Prime numbers upto {0} are {1}".format(n,primelist))

x=input("First n prime numbers: ")
plist=nprimes(int(x))
print("First {0} prime numbers are {1}".format(x,plist))

"""
primesupto(): know we have to scan from 1 to n, use for
nprimes(): Range to scan is not known in advance, use while
"""
