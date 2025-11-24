from math import gcd, isqrt

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def prime_factors(n):
    factors = set()
    
    while n % 2 == 0:
        factors.add(2)
        n //= 2
    # Check odd factors
    for i in range(3, isqrt(n) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n //= i
    if n > 2:
        factors.add(n)
    return factors

def is_carmichael(n):
    if n < 2 or is_prime(n):
        return False
    factors = prime_factors(n)
    
    product = 1
    for f in factors:
        product *= f
    if product != n:
        return False
    
    for p in factors:
        if (n - 1) % (p - 1) != 0:
            return False
    
    for a in range(2, n):
        if gcd(a, n) == 1:
            if pow(a, n - 1, n) != 1:
                return False
    return True

import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")


