def lucas_sequence(n):
    if n <= 0:
        return []
    if n == 1:
        return [2]
    sequence = [2, 1]
    for _ in range(2, n):
        next_value = sequence[-1] + sequence[-2]
        sequence.append(next_value)
    return sequence


import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 

end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")
