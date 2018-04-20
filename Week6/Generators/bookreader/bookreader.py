def pages_gen(path):
    import os
    pages = [page for page in os.listdir(
        path) if os.path.isfile(page) and page.endswith(".txt")]

    yield from sorted(pages)


def load_page(file_):
    with open(file_, "r") as f:
        for line in f:
            yield line


def chapter_gen(iterator):
    last_line = None
    next_line = next(iterator)
    if not last_line:
        print(next_line, end="")
        for line in iterator:
            if line.startswith("# Chapter"):
                last_line = next_line
                next_line = line
                break
            else:
                print(line, end="")
    if "# Chapter" in next_line:
        return next_line


def get_chapter(path):
    for page in pages_gen(path):
        page_gen = load_page(page)
        next_line = None
        while True:
            input_ = input("Press enter: ")
            if input_ == "":
                try:
                    if next_line:
                        print(next_line)
                    next_line = chapter_gen(page_gen)
                    # import pdb
                    # pdb.set_trace()
                except StopIteration:
                    print("Next Page")
                    break
