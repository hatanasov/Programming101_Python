import os
import sys


def duhs(directory):
    size = os.path.getsize(directory)
    try:
        for item in os.scandir(directory):
            if item.is_file():
                size += item.stat().st_size
            elif item.is_dir():
                size += duhs(item.path)
        return size
    except FileNotFoundError:
            return 'No such file or Directory!'


def main():
    dir_checked = sys.argv[1]
    size = duhs(dir_checked)
    result = ''
    if size > 1000000000:
        result = size // (1000 * 1000 * 1024)
        result = str(result) + 'G'
    elif size > 1000000:
        result = size // (1000 * 1024)
        result = str(result) + 'M'
    elif size > 1000:
        # result = size // 1024
        result = str(size) + 'k'

    print('{} size is: {}'.format(dir_checked, result))


if __name__ == '__main__':
    main()
