import time
import tracemalloc

def mean_of_digits(n):
    """Return the average of all digits in a number."""
    if n < 0:
        n = -n
    digits = [int(d) for d in str(n)]
    return sum(digits) / len(digits)

# Example usage
n = 12345

# Start measuring
start_time = time.perf_counter()
tracemalloc.start()

try:
    mean = mean_of_digits(n)
finally:
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

print(f"Mean of digits of {n} = {mean}")
print(f"Execution Time: {end_time - start_time:.8f} seconds")
print(f"Memory Usage: Current = {current} bytes, Peak = {peak} bytes")
