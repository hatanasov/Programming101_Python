def count_substrings(haystack, needle):
    count = 0
    word_list = haystack.split()
    for word in word_list:
        if needle in word:
            count += 1
    return count


def sum_matrix(m):
    sum = 0
    for row in m:
        for num in row:
            sum += num
    return sum


def nan_expand(times):
    nan = 'NaN'
    string = 'Not a '
    if times == 0:
        return '""'
    return '"' + string * times + nan + '"'


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



def group(list_of_thigs):
    from itertools import groupby
    result = []
    for index, element in groupby(list_of_thigs):
        result.append(list(element))
    return result

