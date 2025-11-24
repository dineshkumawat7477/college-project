def mod_exp(base, exponent, modulus):
    if modulus == 1:
        return 0
    result = 1
    base = base % modulus
    while exponent > 0:
        if exponent % 2 == 1:
            result = (result * base) % modulus
        exponent = exponent >> 1  
        base = (base * base) % modulus  
    return result

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("mod_exp(base, exponent, modulus)" , globals=globals() , number = 1000000)
print("runtime =" , runtime/1000000, "seconds")


