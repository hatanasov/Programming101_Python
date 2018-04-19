def chain(iterable_one, iterable_two):
    yield from iterable_one
    yield from iterable_two


def compress(iterable, mask):
    for index, mask in enumerate(mask):
        if mask == True:
            yield iterable[index]


def cycle(iterable):

    while True:
        yield iterable


