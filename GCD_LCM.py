import math
from functools import reduce

def gcd_list(numbers):
    return reduce(math.gcd, numbers)


def lcm_base(x, y):
    return (x * y) // math.gcd(x, y)

def lcm_list(numbers):
    return reduce(lcm_base, numbers, 1)