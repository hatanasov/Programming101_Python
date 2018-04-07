matrix = [[1, 2, 3],
          [4, 5, 6],
          [7, 8, 9]]


def matrix_bombing_plan(m):
    result = {}
    rows = len(m)
    columns = len(m[0])
    for row, row_elements in enumerate(m):
        for column, element in enumerate(row_elements):
            result[(row, column)] = sum_bombed_matrix(m, rows, columns, row, column, element)
    return result


def sum_bombed_matrix(m, rows, columns, r, c, element):
    sum_matrix = 0
    for x in range(rows):
        for y in range(columns):
            mx = m[x][y]
            if x == r and y == c:
                sum_matrix += mx
                continue
            elif x in range(r - 1, r + 2) and y in range(c - 1, c + 2):
                mx -= element
                if mx > 0:
                    sum_matrix += mx
            else:
                sum_matrix += mx
    return sum_matrix


# print(matrix_bombing_plan(matrix))