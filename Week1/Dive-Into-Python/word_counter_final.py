word_matrix = [['i', 'v', 'a', 'n'],
               ['e', 'v', 'n', 'h'],
               ['i', 'n', 'a', 'v'],
               ['m', 'v', 'v', 'n'],
               ['q', 'r', 'i', 't']]

word = ['i', 'v', 'a', 'n']

row = 5
col = 4

def count_word(matrix, word, row, column):
    index = 0

    while index < len(word):
        for r, row_list in enumerate(matrix):
            for c, element in enumerate(row_list):

