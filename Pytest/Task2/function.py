# def is_prime(x):
#     if x == 0 or x == 1:
#         return False
#     for i in range(2, x):
#         if not x % i:
#             return False
#     return True

def is_prime(x):
    if x == 2:
        return True
    if x < 2 or x%2 == 0:
        return False
    i = 3
    while i*i <= x:
        if x%i == 0:
            return False
        i+=2
    return True