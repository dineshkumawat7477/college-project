def is_deficient(n):
    total = 0
    for i in range(1, n):
        if n%i == 0:
            total+=i
    return total<n

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_deficient(n)", globals=globals(), number = 1000000)
print("runtime =", runtime/1000000, "seconds")