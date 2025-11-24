def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def twin_primes(limit):
    twins = []
    for num in range(2, limit - 1):
        if is_prime(num) and is_prime(num + 2):
            twins.append((num, num + 2))
    return twins
