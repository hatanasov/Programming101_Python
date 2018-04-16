from utils.serializers import Jsonable

class Panda(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Person(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


ico = Person(name="Ico", age=30)
ivo = Person(name="Ivo", age=25)
setattr(ico, frend, ivo)
setattr(ivo, frend, ico)
ico_attributs = ico.to_json()
print(ico_attributs)