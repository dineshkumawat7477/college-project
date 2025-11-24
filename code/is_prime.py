def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def is_fibonacci(num):
    
    import math
    return (math.isqrt(5 * num * num + 4) ** 2 == 5 * num * num + 4) or \
           (math.isqrt(5 * num * num - 4) ** 2 == 5 * num * num - 4)

def is_fibonacci_prime(n):
    
    return is_fibonacci(n) and is_prime(n)


import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")
