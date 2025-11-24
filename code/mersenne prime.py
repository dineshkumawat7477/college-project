def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_mersenne_prime(p):
    if not is_prime(p):
        return False
    mersenne_number = 2 ** p - 1
    return is_prime(mersenne_number)
