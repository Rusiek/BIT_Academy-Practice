# Pierwszy zawiera funkcję, która dostaje liczbę "n" i wyznaczą najmniejszą liczbę pierwszą większą od "n".

def is_prime(x):
    if x == 2 or x == 3:
        return True
    if x <= 1 or not x % 2 or not x % 3:
        return False
    i = 5
    while i < int(x**0.5) + 1:
        if not x % i:
            return False
        i += 2
        if not x % i:
            return False
        i += 4
    return True

def function(x):
    x += 1
    while not is_prime(x):
        x += 1
    return x