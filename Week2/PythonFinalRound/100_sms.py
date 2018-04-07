from itertools import groupby

keyboard = {
    2: 'abc',
    3: 'def',
    4: 'ghi',
    5: 'jkl',
    6: 'mno',
    7: 'pqrs',
    8: 'tuv',
    9: 'wxyz'
}

CAPITAL_LETTER = False
WHITE_SPASE = 0
BREAK_NUM = -1


def group(list_of_thigs):
    result = []
    for index, element in groupby(list_of_thigs):
        result.append(list(element))
    return result


def numbers_to_message(pressed_sequence):
    grouped_seq = group(pressed_sequence)
    message = ''
    for seq in grouped_seq:
        if seq[0] == 1:
            CAPITAL_LETTER = True
            continue
        elif seq[0] == WHITE_SPASE:
            message += ' '
            continue
        elif seq[0] == BREAK_NUM:
            continue
        else:
            if len(seq) > len(keyboard[seq[0]]):
                coefficient = len(seq) // len(keyboard[seq[0]])
                char_position = (len(seq) - ((len(keyboard[seq[0]]) * coefficient) + 1))
            else:
                char_position = len(seq) - 1
            letter = keyboard[seq[0]][char_position]
            if CAPITAL_LETTER:
                message += letter.upper()
            else:
                message += letter
            CAPITAL_LETTER = False

    return message

# print(numbers_to_message([1, 4, 4, 4, 8, 8, 8,8,8,8,8,8,8, 6, 6, 6, 0, 3, 3, 0, 1, 7, 7, 7, 7, 7, 2, 6, 6, 3, 2]))


def message_to_numbers(message):
    message_to_list = [char for char in message]
    result = []
    last_key = 0
    for char in message_to_list:
        if char == ' ':
            result.append(0)
            continue
        elif char.isupper():
            result.append(1)
            char = char.lower()
        for key, value in keyboard.items():
            if last_key == key and char in value:
                result.append(-1)
            if char in value:
                multiply = value.index(char) + 1
                temp_list = [key for num in range(multiply)]
                result += temp_list
                last_key = key
    return result
#
# print(message_to_numbers('Ivo e Panda'))
# print(message_to_numbers("abc"))
# print(message_to_numbers("aabbcc"))
