def is_credit_card_valid(number):
    num_reversed = [int(num) for num in str(number)]
    num_reversed = num_reversed[::-1]
    sum_number = 0
    if len(num_reversed) % 2 == 0:
        return False
    for index, digit in enumerate(num_reversed):
        if index == 0:
            sum_number += digit
        elif index % 2 == 0:
            sum_number += digit
        else:
            sum_number += digit * 2
    print(sum_number)
    if sum_number % 10 == 0:
        return True
    else:
        return False


print(is_credit_card_valid(79927398713))
print(is_credit_card_valid(79927398715))