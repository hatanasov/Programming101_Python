def sum_matrix(m):
    sum = 0
    for row in m:
        for num in row:
            sum += num
    return sum

# m = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# print(sum_matrix(m))
# m = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
# print(sum_matrix(m))
# m = [[1, 2], [3, 4], [5, 6], [7, 8], [9, 10]]
# print(sum_matrix(m))
