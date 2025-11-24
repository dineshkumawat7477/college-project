def mod_inverse(a, m):
    def egcd(a, b):
        if a == 0:
            return b, 0, 1
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y

    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception('Inverse does not exist')
    else:
        return x % m

def crt(remainders, moduli):
   
    if len(remainders) != len(moduli):
        raise ValueError("Lists remainders and moduli must be of the same length")
    
    M = 1
    for m in moduli:
        M *= m

    x = 0
    for r_i, m_i in zip(remainders, moduli):
        M_i = M // m_i
        inv = mod_inverse(M_i, m_i)
        x += r_i * inv * M_i
    return x % M


import time

start_time = time.perf_counter()

for i in range(1000000):
    result = i * 2 
end_time = time.perf_counter()
elapsed_time = end_time - start_time

print(f"Elapsed time: {elapsed_time:.6f} seconds")

