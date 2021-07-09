# -*- coding: utf-8 -*-
"""
Created on Mon Jul  5 21:29:09 2021
"""

import timeit
setup_code = ''
statement="""
for i in range(10000000):
    m=i+1
print(m)
"""
print(f"Execution time is: {timeit.timeit(setup=setup_code, stmt=statement, number=1)}")

