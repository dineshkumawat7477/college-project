import random

def is_prime_miller_rabin(n, k):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    
    
    r = 0
    d = n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    def miller_test(a, d, n, r):
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            return True
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                return True
        return False
    for _ in range(k):
        a = random.randint(2, n - 2)
        if not miller_test(a, d, n, r):
            return False
    return True

def mod_inverse(a, m):
    
    a = a % m
    if a == 0:
        return None  

    m0, x0, x1 = m, 0, 1
    while a > 1:
        q = a // m
        a, m = m, a % m
        x0, x1 = x1 - q * x0, x0

    if x1 < 0:
        x1 += m0
    return x1

import time

start_time = time.perf_counter()
for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")
