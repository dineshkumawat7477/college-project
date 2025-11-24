def divisor_count(x):
    count = 0
    for i in range(1, int(x**0.5) + 1):
        if x % i == 0:
            count += 1
            if i != x // i:
                count += 1
    return count

def is_highly_composite(n):
    n_divisors = divisor_count(n)
    for i in range(1, n):
        if divisor_count(i) >= n_divisors:
            return False
    return True

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("divisor_count(x)" , globals=globals() , number = 1000000)
print("runtime =" , runtime/1000000, "seconds")
