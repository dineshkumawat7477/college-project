def order_mod(a, n):
    
    if gcd(a, n) != 1:
        raise ValueError("a and n must be coprime for multiplicative order to exist")
    k = 1
    mod_result = a % n
    while mod_result != 1:
        mod_result = (mod_result * a) % n
        k += 1
    return k

def gcd(x, y):
    while y:
        x, y = y, x % y
    return x

import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")
