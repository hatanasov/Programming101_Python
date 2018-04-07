def get_prime_factor(n):
    """2 is the only even prime number"""
    if n % 2 == 0:
        return 2
    for num in range(3, n + 1, 2):
        if n % num == 0:
            return num


def goldbach(n):
    prime_nums = set()
    num = n
    while n != 2:
        prime = get_prime_factor(n)
        prime_nums.add(prime)
        n -= 1
    result = sorted(list({tuple(sorted([x, y])) for x in prime_nums for y in prime_nums if x + y == num}))

    return result


# print(goldbach(10))
# print(goldbach(100))