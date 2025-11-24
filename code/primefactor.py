def prime_factors(n):
    factors = []
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    i = 3

    #runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_prime Factor(n)", globals=globals(), number = 1000000)
print("runtime =", runtime/1000000, "seconds")





