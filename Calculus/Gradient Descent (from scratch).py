# -*- coding: utf-8 -*-
"""
Created on Sun Mar 20 01:01:28 2022

@author: bharath.setty
"""

def next_step(V, direction, step_size):
    return [v_i + step_size*-1*direction_i for v_i, direction_i in zip(V,direction)]

def minimize(f, grad_f, X_0, tolerance=0.05):
    X=X_0
    f_X = f(X)
    grad_f_X = grad_f(X)
    
    while True:
       # print(X)
        next_X = next_step(X, grad_f_X, 0.5)
        next_f_X = f(next_X)
        if abs(next_f_X - f_X) < tolerance:
            return next_X
        else:
            X, f_X, grad_f_X  = next_X, next_f_X, grad_f(next_X)
            
def f(X):
    return X[0]**2 - (X[0]*X[1]) + X[1]**2

def grad_f(X):
    return [2*X[0]-X[1], -X[0]+2*X[1]]