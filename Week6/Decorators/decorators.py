from functools import wraps
import string


def accepts(*args):
    def accept_func(func):
        @wraps(func)
        def check_type(*other_args):
            check_types = [arg for arg in args]
            for arg in other_args:
                if type(arg) not in check_types:
                    raise TypeError("Argument 1 of say_hello is not str!")
            return func(*other_args)
        return check_type
    return accept_func


def encrypt(key):
    def encrypter(func):
        @wraps(func)
        def decorated():
            message = func()
            alphabet_lower = string.ascii_lowercase
            alphabet_upper = string.ascii_uppercase
            shifted_alphabet_lower = alphabet_lower[key:] + \
                alphabet_lower[:key]
            shifted_alphabet_upper = alphabet_upper[key:] + \
                alphabet_upper[:key]
            lower_table = str.maketrans(alphabet_lower, shifted_alphabet_lower)
            upper_table = str.maketrans(alphabet_upper, shifted_alphabet_upper)
            result_str = message.translate(lower_table).translate(upper_table)
            return result_str
        return decorated
    return encrypter


def log(log_file):
    def logger(origin_func):
        @wraps(origin_func)
        def decorated():
            import logging
            from datetime import datetime
            now = str(datetime.now())
            origin_func_name = origin_func.__name__
            with open(log_file, "a") as f:
                log = "{} was called ad {}\n".format(origin_func_name, now)
                f.write(log)
            return origin_func()
        return decorated
    return logger


def performance(log_file):
    def logger(origin_func):
        @wraps(origin_func)
        def decorated_logger():
            import datetime
            t1 = datetime.datetime.now()
            origin_func()
            t2 = datetime.datetime.now()
            time = t2 - t1
            with open(log_file, "a") as f:
                log = "{} was called and took {} seconds to complete\n".format(
                    origin_func.__name__, time.total_seconds())
                f.write(log)
        return decorated_logger
    return logger


# @accepts(str)
# def say_hello(name):
#     return "Hello, I am {}".format(name)


# print(say_hello("Ico"))
# print(say_hello(10))

# @accepts(str, int)
# def deposit(name, money):
#     print("{} sends {} $!".format(name, money))
#     return True


# print(say_hello("ico"))
# say_hello(4)
# print(deposit("RadoRado", 10))
# print(deposit("ico", {"age": 10}))


# @log("logs.txt")
# @encrypt(2)
# def get_low():
#     return "Get get get low"


# get_low()


# @performance('logs.txt')
# def something_heavy():
#     from time import sleep
#     sleep(2)
#     return "I am done!"


# @performance('logs.txt')
# def get_low():
#     return "Get get get low"


# something_heavy()
# get_low()
