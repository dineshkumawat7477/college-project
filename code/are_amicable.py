def aliquot_sum(n):
    if n < 2:
        return 0
    total = 1
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            total += i
            other = n // i
            if other != i and other != n:
                total += other
    return total

def are_amicable(a, b):
    return aliquot_sum(a) == b and aliquot_sum(b) == a

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("aliquot_sum(n)" , globals=globals() , number = 1000000)
print("runtime =" , runtime/1000000, "seconds")
