def collatz_length(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer")
    steps = 0
    while n != 1:
        if n % 2 == 0:
            n //= 2
        else:
            n = 3 * n + 1
        steps += 1
    return steps

import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")

