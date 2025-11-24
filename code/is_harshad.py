def is_harshad(n):
    if n == 0:
        return False  # 0 is not considered a Harshad number
    digit_sum = sum(int(digit) for digit in str(abs(n)))
    return n % digit_sum == 0

#runtime
import timeit
n = int(input("Enter number: "))
runtime = timeit.timeit("is_harshad(n)", globals=globals(), number = 1000000)
print("runtime =", runtime/1000000, "seconds")
