def legendre_symbol(a, p):
    if a % p == 0:
        return 0
    ls = pow(a, (p - 1) // 2, p)
    if ls == 1:
        return 1
    if ls == p - 1:
        return -1
    return 0  
