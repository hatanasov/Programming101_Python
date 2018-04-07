def is_number_balanced(number):
    digits = [int(num) for num in str(number)]
    if len(digits) == 1:
        return True
    len_of_digit = len(digits)

    left = 0
    for index in range(len_of_digit // 2):
        left += int(digits[index])

    right = 0
    for index in range(1, (len_of_digit // 2) + 1):
        index *= -1
        right += int(digits[index])

    if left == right:
        return True
    else:
        return False


def increasing_or_decreasing(seq):
    coppy_list = seq[1:]
    is_increasing = all([el > seq[index]
                         for index, el in enumerate(coppy_list)])
    is_decreasing = all([el < seq[index]
                         for index, el in enumerate(coppy_list)])
    if is_increasing:
        return 'Up!'
    elif is_decreasing:
        return 'Down!'
    else:
        return False
# print(increasing_or_decreasing([1,2,3,4,5]))
# print(increasing_or_decreasing([5,4,3,2,1,2]))


def get_largest_palindrome(n):
    n = n - 1
    num = str(n)
    while num != num[::-1]:
        n -= 1
        num = str(n)
    return n

# print(get_largest_palindrome(754649))


def sum_of_numbers(input_string):
    import re
    num_in_str = re.findall(r'\d+', input_string)
    result = 0
    for num in num_in_str:
        result += int(num)
    return result

# print(sum_of_numbers("ab125cd3"))


def birthday_ranges(birthdays, ranges):
    result = []
    count = 0
    for day_range in ranges:
        start_day, end_day = day_range[0], day_range[1] + 1
        for b_day in birthdays:
            if b_day in range(start_day, end_day):
                count += 1
        result.append(count)
        count = 0
    return result


# print(birthday_ranges([1, 2, 3, 4, 5], [(1, 2), (1, 3), (1, 4), (1, 5), (4, 6)]))
# print(birthday_ranges([5, 10, 6, 7, 3, 4, 5, 11, 21, 300, 15], [(4, 9), (6, 7), (200, 225), (300, 365)]))
