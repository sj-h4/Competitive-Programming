import math
def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    for p in range(3, int(math.sqrt(n))+1, 2):
        if n % p == 0:
            return False

    return True
