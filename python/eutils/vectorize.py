import functools
import operator

def v_prod(x):
    return functools.reduce(operator.mul, x)

def v_sum(x):
    return functools.reduce(operator.add, x)