import random
import string


def gen_word():
    alphabet = string.ascii_lowercase
    len_ = random.randint(1, 20)
    while True:
        word = ""
        for num in range(len_):
            word += random.choice(alphabet)
        yield word


def gen_sentence():
    word_gen = gen_word()
    punct_char = ".,!?"
    last_punct_char = ""
    len_sentence = random.randint(1, 50)
    pass


def gen_chapter():
    pass


def gen_book(chapter_count, chapter_lenght):
    pass
