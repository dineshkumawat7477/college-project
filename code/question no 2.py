import time
import tracemalloc

def is_palindrome(n):
    """Check if a number reads the same forwards and backwards."""
    n_str = str(n)  # Convert number to string
    return n_str == n_str[::-1]  # Compare with its reverse

# Example usage
n = 12321  # change this number to test others

# Start measuring time and memory
start_time = time.perf_counter()
tracemalloc.start()

try:
    result = is_palindrome(n)
finally:
    # Stop measuring memory
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    end_time = time.perf_counter()

print(f"Is {n} a palindrome? {result}")
print(f"Execution Time: {end_time - start_time:.8f} seconds")
print(f"Memory Usage: Current = {current} bytes, Peak = {peak} bytes")
