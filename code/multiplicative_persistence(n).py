def multiplicative_persistence(n):
    steps = 0
    while n >= 10:  # Continue until single digit
        product = 1
        for digit in str(n):
            product *= int(digit)
        n = product
        steps += 1
    return steps
print(multiplicative_persistence(78))


