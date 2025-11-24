def is_prime_power(n):
    if n < 2:
        return False
    for k in range(1, n.bit_length() + 1):
        root = int(round(n ** (1.0 / k)))
        if root ** k == n:

            if root < 2:
                continue
            for i in range(2, int(root ** 0.5) + 1):
                if root % i == 0:
                    break
            else:
                return True
    return False
