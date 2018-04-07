from itertools import groupby


def group(list_of_thigs):
    result = []
    for index, element in groupby(list_of_thigs):
        result.append(list(element))
    return result


#
# print(group([1, 1, 1, 2, 3, 1, 1]))
# print(group([1, 2, 1, 2, 3, 3]))
