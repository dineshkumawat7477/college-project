def is_pronic(n):
    if n < 0:
        return False  # Only non-negative numbers can be pronic
    i = 0
    while i * (i + 1) <= n:
        if i * (i + 1) == n:
            return True
        i += 1
    return False

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_pronic(n)", globals=globals(), number = 1000000)
print("runtime =", runtime/1000000, "seconds")
