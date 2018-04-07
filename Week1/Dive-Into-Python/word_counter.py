def input_table():
    word = [char for char in input()]
    table_parameters = [int(num) for num in input().split()]
    word_table = []

    while True:
        row = input().split()
        if not row:
            break
        word_table.append(row)

    if len(word) > len(word_table) or len(word) > len(word_table[0]):
        print('Invalid number of rows or columns!')
    else:
        result = 0
        for row_index, row in enumerate(word_table):
            for column_index, element in enumerate(row):
                if element != 'checked':
                    find_words(word_table, word, element)
                    result += 1
    print(word)
    print(word_table)
    return result


def find_words(matrix, word, element):
    word_index = 0
    searched_word = []
    for r, row in enumerate(matrix):
        for c, cur_element in enumerate(row):
            if cur_element == word[word_index]:
                searched_word.append((r, c))
                if


input_table()
