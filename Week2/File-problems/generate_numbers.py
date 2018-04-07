import sys
from random import randint


def generate_numbers(filename, numbers):
    with open(filename, 'w') as wf:
        for i in range(int(numbers)):
            num = randint(1, 1000)
            wf.write('{} '.format(num))


def main():
    file_to_write = sys.argv[1]
    rand_num_generates = sys.argv[2]
    generate_numbers(file_to_write, rand_num_generates)


if __name__ == '__main__':
    main()
