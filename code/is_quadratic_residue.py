def is_quadratic_residue(a, p):
    
    if a % p == 0:
        return True  
    
    legendre = pow(a, (p - 1) // 2, p)
    return legendre == 1

import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")
