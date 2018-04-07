def filter_by(data, **kwargs):
    result = []
    search = [{key: str(kwargs[key])} for key in kwargs]
    if len(search) == 1:
        result = [person for key, value in search[0].items() for person in data if person[key] == value]
        # print(result)
    elif len(search) > 1:
        result = [person for key, value in search[0].items() for person in data if person[key] == value]
        search.pop(0)
        result = filter_by(result, **search[0])
    return result


def startswith(data, **kwargs):
    kwarg = kwargs
    search_key = [key.split('__') for key in kwarg.keys()]
    search = {search_key[0][0]: kwargs[search_key[0][0] + '__' + search_key[0][1]]}
    starts = [person for key, value in search.items() for person in data if person[key].startswith(value)]
    return starts


def contains(data, **kwargs):
    kwarg = kwargs
    search_key = [key.split('__') for key in kwarg.keys()]
    search = {search_key[0][0]: kwargs[search_key[0][0] + '__' + search_key[0][1]]}
    result = [person for key, value in search.items() for person in data if value in person[key]]

    return result


def interval_search(data, **kwargs):
    new_key = [key.split('__') for key in kwargs.keys()]
    values = [value for value in kwargs.values()]
    new_kwargs = {new_key[0][0]: values}

    result = [people for key, values in new_kwargs.items() for people in data
              if int(people[key]) in range(values[0], values[1])]
    return result


def interval_search_ordered(data, **kwargs):
    unordered = interval_search(data, **kwargs)
    ordered_by = {key: value for key, value in kwargs.items() if key == 'order_by'}
    result = sorted(unordered, key=lambda x: x[ordered_by['order_by']])
    return result


def filter_count(data, **kwargs):
    return len(filter(data, **kwargs))


def filter_first(data, **kwargs):
    return filter(data, **kwargs)[0]


def filter_last(data, **kwargs):
    return filter(data, **kwargs)[-1]


def filter(csv_file, **kwargs):
    data = file_to_dict(csv_file)
    all_kwargs = [key for key in kwargs.keys()]
    result = []
    if not all_kwargs:
        return result
    else:
        if 'salary__gt' in all_kwargs and 'salary__lt' in all_kwargs and 'order_by' in all_kwargs:
            result = interval_search_ordered(data, **kwargs)
        elif 'salary__gt' in all_kwargs and 'salary__lt' in all_kwargs and 'order_by' not in all_kwargs:
            result = interval_search(data, **kwargs)
        elif '_startswith' in all_kwargs[0]:
            print(all_kwargs)
            result = startswith(data, **kwargs)
        elif '__contains' in all_kwargs[0]:
            result = contains(data, **kwargs)
        else:
            result = filter_by(data, **kwargs)
    result_to_list = []
    for line in result:
        person_info = [person for person in line.values()]
        result_to_list.append(person_info)
    return result_to_list


def file_to_dict(csv_file):
    import csv
    with open(csv_file, 'r') as f:
        reader = csv.DictReader(f)
        data_list = [line for line in reader]

    return data_list


#
# test_filter = filter('short.csv', salary__gt=0, salary__lt=2000, order_by='salary')
# test_filter = filter('short.csv', favourite_color='white', full_name='Hristo Atanasov')
# test_filter = filter_by('short.csv')
# print(test_filter)
