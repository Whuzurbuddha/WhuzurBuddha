import sympy as sp

def count_primes_less_than(n: int) -> int:
    prime_vec = []
    for i in range(1, n + 1):
        check = sp.isprime(i)
        if check:
            prime_vec.append(i)
    return prime_vec.__len__()
print("Enter a number: ")
input = int(input())
output = count_primes_less_than(input)
print(output)
