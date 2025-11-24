def is_perfect_power(n):
    if n <= 1:
        return True  

    
    max_b = n.bit_length()  
    for b in range(2, max_b + 1):
        a = round(n ** (1 / b))

        if a**b == n or (a+1)**b == n or (a-1)**b == n:
            if a > 0:
                return True
    return False

import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")


