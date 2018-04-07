from group_numbers import group


def max_consecutive(items):
    groups = group(items)
    len_groups = [len(element) for element in groups]
    return max(len_groups)

# print(max_consecutive([1, 2, 3, 3, 3, 3, 4,4,4,4,4,4,44,6, 3, 3]))
