import functools
import operator

def v_prod(x):
    return functools.reduce(operator.mul, x)