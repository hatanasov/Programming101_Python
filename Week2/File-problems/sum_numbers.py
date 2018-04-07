def sum_numbers():
    import sys

    filename = sys.argv[1]
    with open(filename, 'r') as f:
        nums = sum([int(num) for num in f.read().split()])

    print(nums)


if __name__ == '__main__':
    sum_numbers()
