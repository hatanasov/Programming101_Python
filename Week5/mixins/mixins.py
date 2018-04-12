from utils.serializers import Jsonable

class Panda(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age

