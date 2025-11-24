import time
import tracemalloc

def digital_root(n):
    """Return the digital root of a number (sum of digits until one digit remains)."""
    if n < 0:
        n = -n  # handle negative numbers

    while n >= 10:  # repeat until only one digit remains
        n = sum(int(d) for d in str(n))
    return n

# Example usage
n = 9875  # try changing this number

# Start measuring time and memory
start_time = time.perf_counter()
tracemalloc.start()

try:
    result = digital_root(n)
finally:
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

print(f"Digital root of {n} = {result}")
print(f"Execution Time: {end_time - start_time:.8f} seconds")
print(f"Memory Usage: Current = {current} bytes, Peak = {peak} bytes")
