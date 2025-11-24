def partition_function(n):
    p = [0] * (n+1)
    p[0] = 1
    for i in range(1, n+1):
        total = 0
        k = 1
        while True:
            pent1 = k * (3*k - 1) // 2
            pent2 = k * (3*k + 1) // 2
            if pent1 > i and pent2 > i:
                break
            sign = -1 if (k % 2 == 0) else 1
            if pent1 <= i:
                total += sign * p[i - pent1]
            if pent2 <= i:
                total += sign * p[i - pent2]
            k += 1
        p[i] = total
    return p[n]

import time

start_time = time.perf_counter()
for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()

elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time:.6f} seconds")

