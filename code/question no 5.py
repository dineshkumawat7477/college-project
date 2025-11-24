import time
import tracemalloc

def is_abundant(n):
    """Return True if the sum of proper divisors of n is greater than n."""
    if n < 1:
        return False  # no such thing as abundant or negative numbers

    divisors_sum = 1  # start with 1 since it's always a proper divisor
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            divisors_sum += i
            if i != n // i:  # avoid adding the square root twice
                divisors_sum += n // i

    return divisors_sum > n

# Example usage
n = 12  # 12 is abundant since 1 + 2 + 3 + 4 + 6 = 16 > 12

# Start measuring time and memory
start_time = time.perf_counter()
tracemalloc.start()

try:
    result = is_abundant(n)
finally:
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

print(f"Is {n} an abundant number? {result}")
print(f"Execution Time: {end_time - start_time:.8f} seconds")
print(f"Memory Usage: Current = {current} bytes, Peak = {peak} bytes")
