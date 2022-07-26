def is_prime(x):
    if x <= 1:
        return False
    for i in range(2, int(x**0.5+1)):
        if not x % i:
            return False
        
    return True
