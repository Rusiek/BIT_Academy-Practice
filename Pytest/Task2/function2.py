from math import sqrt


def is_prime2(n):
    if n <= 0:
        return False
    if n == 2:
        return True
    if n == 1 or n % 2 == 0:
        return False
    for i in range(3, int(sqrt(n))+1):
        if n % i == 0:
            return False
    return True

print(is_prime2(1))