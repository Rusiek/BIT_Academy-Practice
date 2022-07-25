def is_prime(x):
    if x <= 1:
        return False

    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False

    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i+2) == 0:
            return False
        i += 6
    return True 


def next_primary(n):
    n += 1
    while is_prime(n) == False:
        n += 1
    return n