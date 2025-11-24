def eta_approx(s, terms):
    total = 0
    for n in range(1, terms + 1):
        total += 1 / (n ** s)
    return total

import time

start_time = time.perf_counter()
for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")



