def sol(n):
    
    if n == 2 or n == 3:
        return True
    if n <= 1 or n % 2 == 0 or n % 3 == 0:
        return False
    for i in range(6, int(n**0.5 + 1), 6):
        if n % (i - 1) == 0 or n % (i + 1) == 0:
            return False
    return True
