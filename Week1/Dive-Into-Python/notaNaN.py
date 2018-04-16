def nan_expand(times):
    nan = 'NaN'
    string = 'Not a '
    if times == 0:
        return '""'
    return '"' + string * times + nan + '"'

# print(nan_expand(4))
