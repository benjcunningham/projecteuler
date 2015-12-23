import functools
import operator

def v_prod(x):
    if len(x) < 1:
        return 0
    return functools.reduce(operator.mul, x)

def v_sum(x):
    if len(x) < 1:
        return 0
    return functools.reduce(operator.add, x)