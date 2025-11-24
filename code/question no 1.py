import time
import tracemalloc

def factorial(n):
    """Return the factorial of a non-negative integer n."""
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

# Example usage
n = 10  # Change this to test other numbers

# Start measuring time and memory
start_time = time.perf_counter()
tracemalloc.start()

fact = factorial(n)

# Stop measuring memory and time
current, peak = tracemalloc.get_traced_memory()
tracemalloc.stop()
end_time =
