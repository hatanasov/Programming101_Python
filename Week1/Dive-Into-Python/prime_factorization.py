def get_prime_factor(n):
    """2 is the only even prime number"""
    if n % 2 == 0:
        return 2
    for num in range(3, n + 1, 2):
        if n % num == 0:
            return num


def prime_factorization(digit):
    number = abs(digit)
    prime_factors = {}
    result = []
    while number > 1:
        prime = get_prime_factor(number)
        if prime in prime_factors:
            prime_factors[prime] += 1
        else:
            prime_factors[prime] = 1
        number //= prime
    for key, value in prime_factors.items():
        result.append((key, value))
    return result


print(prime_factorization(86))
