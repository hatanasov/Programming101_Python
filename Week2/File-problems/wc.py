import sys


def wc(comand, file):
    with open(file, 'r') as f:
        f_content = f.read()
        lines = [line for line in f_content.split('\n')]
        words = [word for line in lines for word in line.split(' ') if word]

        if comand == 'lines':
            print(len(lines) - 1)
            print(lines)
        elif comand == 'words':
            print(len(words))
            print(words)
        elif comand == 'chars':
            print(len(f_content))


def main():
    comand, file_check = sys.argv[1], sys.argv[2]
    return wc(comand, file_check)


if __name__ == '__main__':
    main()
