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
