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


# @accepts(str)
# def say_hello(name):
#     return "Hello, I am {}".format(name)


# @accepts(str, int)
# def deposit(name, money):
#     print("{} sends {} $!".format(name, money))
#     return True

# print(say_hello("ico"))
# say_hello(4)
# print(deposit("RadoRado", 10))
# print(deposit("ico", {"age": 10}))



def encrypt(key):
    def encrypter(func):
        def decorated():
            message = func()
            alphabet_lower = string.ascii_lowercase
            alphabet_upper = string.ascii_uppercase
            shifted_alphabet_lower = alphabet_lower[key:] + alphabet_lower[:key]
            shifted_alphabet_upper = alphabet_upper[key:] + alphabet_upper[:key]
            lower_table = str.maketrans(alphabet_lower, shifted_alphabet_lower)
            upper_table = str.maketrans(alphabet_upper, shifted_alphabet_upper)
            result_str = message.translate(lower_table).translate(upper_table)
            return result_str
        return decorated
    return encrypter


@encrypt(2)
def get_low():
    return "Get get get low"


print(get_low())

