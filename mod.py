def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
    
import numpy as np

def sinc2d(x, y):
    if x == 0.0 and y == 0.0:
        return 1.0
    elif x == 0.0:
        return np.sin(y) / y
    elif y == 0.0:
        return np.sin(x) / x
    else:
        return (np.sin(x) / x) * (np.sin(y) / y)
    
def a(x):
    return x + 1

def b(x):
    return 2 * x

def c(x):
    return b(a(x))

def std(vals):
    return np.std(vals)