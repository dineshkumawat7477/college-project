import random
import math

def pollard_rho(n):
    if n % 2 == 0:
        return 2
    if n == 1:
        return n
    if is_prime_miller_rabin(n, 5):  
        return n
    while True:
        x = random.randint(2, n-1)
        y = x
        c = random.randint(1, n-1)
        d = 1
        f = lambda x: (x*x + c) % n
        while d == 1:
            x = f(x)
            y = f(f(y))
            d = math.gcd(abs(x-y), n)
        if d != n:
            return d

import time

start_time = time.perf_counter()
for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")


