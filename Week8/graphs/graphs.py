def iter_over_iterable(data, key):
    """data is some iterable, from above type"""
    iterables = [tuple, set, list, ord]
    if type(data) in iterables:
        for element in data:
            if type(element) in iterables:
                return iter_over_iterable(element, key)
            elif type(element) is dict:
                return deep_find(element, key)


def deep_find(data, key):
    result = None

    if key in data:
        return data[key]
    for k, v in data.items():
        if type(v) is dict:
            result = deep_find(v, key)
        else:
            result = iter_over_iterable(v, key)
        if result:
            return result
    return result


def deep_find_all(data, key):
    result = []
    if key in data:
        result.append(data[key])
    for k, v in data.items():
        if type(v) is dict:
            value = deep_find(v, key)
            if value:
                result.append(value)
        else:
            value = iter_over_iterable(v, key)
            if value:
                result.append(value)
    if result:
        return result
    return []


def iterator(d, key, val):
    iterables = [tuple, set, list, ord]
    if type(d) in iterables:
        for element in d:
            if type(element) is dict:
                deep_update(element, key, val)
            else:
                iterator(element, key, val)


def deep_update(data, key, val):
    # import pdb
    # pdb.set_trace()
    for k, v in data.items():
        if k == key:
            data[k] = val
        elif type(v) is dict:
            deep_update(v, key, val)
        else:
            iterator(v, key, val)
    return data


def deep_apply(func, data):
    pass


def deep_compare(obj1, obj2):
    pass


def schema_validator(schema, data):
    pass
