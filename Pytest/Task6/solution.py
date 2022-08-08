# solution.py - plik ma zawierać funkcję sprawdzającą czy zadana liczba jest pierwsza

def is_prime(x):
    if x == 2:
        return True
    elif x < 2 or x % 2 == 0 :
        return False
    for i in range(3, int(x**0.5)+1):
        if x % i == 0:
            return False
    return True