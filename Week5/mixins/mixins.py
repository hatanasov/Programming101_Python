from utils.serializers import Jsonable


class Panda(Jsonable):
    # def __init__(self):
    #     self.name = name
    #     self.age = age
    pass


class Person(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


# p = Panda("ivo", 25)
# p_json = p.to_json()

# human = Person("ivo", 25)

# print(p_json)
# print(p == human)
# p1 = Panda.from_json('{"dict": {"name": "Ico", "age": 30}}')
# p2 = Panda.from_json('{"dict": {"name": "Poo", "age": 20}}')
# p1.frend = p2
# print(p1.name)
# print(p1.age)
# print(p1.to_json())
