def polygonal_number(s, n):
    if s < 3 or n < 1:
        raise ValueError("Number of sides must be at least 3 and term number should be positive")
    return ((s - 2) * n * n - (s - 4) * n) // 2


import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")

