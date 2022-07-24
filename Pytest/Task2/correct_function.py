def is_prime(x):
    if x == 0 or x == 1:
        return False
    if x == 2:
        return True
    if x % 2 == 0:
        return False

    i = 3
    while i * i <= x:
        if x % i == 0:
            return False
        i += 1
    return True 