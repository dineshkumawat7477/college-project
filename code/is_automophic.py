def is_automorphic(n):
    squared = n ** 2
    return str(squared).endswith(str(n))

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_automorphic(n)", globals=globals(), number = 1000000)
print("runtime =", runtime/1000000, "seconds")

