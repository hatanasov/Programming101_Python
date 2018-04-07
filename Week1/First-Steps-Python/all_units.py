def sum_of_digits(n):
    if n < 0:
        n *= -1

    result = 0
    list_of_digit = [int(num) for num in str(n)]
    for num in list_of_digit:
        result += num
    return result


def to_digits(n):
    list_of_digits = [int(num) for num in str(n)]
    return list_of_digits


def to_number(digits):
    str_number = ''.join([str(n) for n in digits])
    return int(str_number)


def factorial(num):
    result = 1
    for i in range(1, num + 1):
        result *= i
    return result


def fact_digits(n):
    digits = [int(num) for num in str(n)]
    result = 0
    for num in digits:
        result += factorial(num)
    return result


def fibonacci(n):
    fib_list = [1, 1]
    if n == 1:
        return fib_list[:1]
    elif n == 2:
        return fib_list
    else:
        a = fib_list[0]
        b = fib_list[1]
        while len(fib_list) != n:
            next_element = a + b
            fib_list.append(next_element)
            a = b
            b = next_element
    return fib_list


def fib_numbers(num):
    fib_num = fibonacci(num)
    fib_num_to_str = ''.join([str(num) for num in fib_num])
    return int(fib_num_to_str)


def palindrome(n):
    n = str(n)
    n_list = [i for i in n]
    if n_list == n_list[::-1]:
        return True
    else:
        return False


def count_vowels(some_string):
    vowels = 'aeiouy'
    count = 0
    for char in some_string.lower():
        if char in vowels:
            count += 1
    return count


def count_consonants(some_string):
    consonants = 'bcdfghjklmnpqrstvwxz'
    count = 0
    for char in some_string.lower():
        if char in consonants:
            count += 1
    return count


def char_histogram(some_string):
    histogram = {}
    for char in some_string:
        if char in histogram:
            histogram[char] += 1
        else:
            histogram[char] = 1
    return histogram
