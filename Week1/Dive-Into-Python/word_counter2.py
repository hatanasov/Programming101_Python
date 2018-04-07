def word_count(matrix, word, word_index):
    char_positions = {}
    for r, row in enumerate(matrix):
        for c, element in enumerate(row):
            while word_index < len(word):
                if element == word[word_index]:
                    if element in char_positions:
                        char_positions[element].append((r, c))
                    else:
                        char_positions[element] = [(r, c)]
            word_index += 1
    return char_positions


index = 0
match_word = []
curr_dict = word_count([['i', 'v', 'a', 'n'],
                        ['e', 'v', 'n', 'h'],
                        ['i', 'n', 'a', 'v'],
                        ['m', 'v', 'v', 'n'],
                        ['q', 'r', 'i', 't']], ['i', 'v', 'a', 'n'], index)
print(curr_dict)

# if index != 0:
#     for last_tup in last_dict[f_word[index - 1]]:
#         last_r, last_c = last_tup
#         for tup in curr_dict[f_word[index]]:
#             r, c = tup
#             if (r == last_r and c == last_c + 1) or (r == last_r + 1 and c == last_c) or \
#                     (r == last_r + 1 and c == last_c + 1):
#                 word_set.add(last_tup)
#                 word_set.add(tup)
#             # else:
#             #     word_set.remove(tup)

