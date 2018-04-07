def main():
    import sys
    import os

    try:
        filename = sys.argv[1]
        print(filename)
        if os.access(filename, os.R_OK):
            with open(filename, 'r') as f:
                f_content = f.read()
                print(f_content)
        elif filename not in os.listdir():
            print('No such file "{}"'.format(filename))
        else:
            print("You don't have permission to open {}".format(filename))

    except IndexError:
        print('Error in execution command.')
        print('Usage: "python3 cat.py <filename>"')

if __name__ == '__main__':
    main()

