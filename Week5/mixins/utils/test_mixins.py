import unittest
from serializers import Jsonable
import json


class Frends(Jsonable):
    def __init__(self):
        self.name = 'Poo'


class Panda(Jsonable):
    def __init__(self):
        self.name = 'ivo'
        self.age = 25
        # self.food = ['bambuk', 'mint']


class Person(Jsonable):
    def __init__(self, name, age):
        self.name = name
        self.age = age


class TestJsonable(unittest.TestCase):
    def setUp(self):
        self.ivo_panda = Panda()
        self.ivo_panda_dict = self.ivo_panda.to_json()
        self.expexted = {
            "class_name": self.ivo_panda.__class__.__name__,
            "dict": self.ivo_panda.__dict__
        }

    def test_to_json(self):
        self.assertEqual(self.ivo_panda_dict,
                         json.dumps(self.expexted, indent=4))

    def test_to_json_works_with_instances_of_other_classes(self):
        self.ivo_panda.frend = Frends()

        ivo_panda_dict = self.ivo_panda.to_json()

        dict_ = self.ivo_panda.__dict__

        dict_['frend'] = {
            'class_name': 'Frends',
            'dict': {'name': 'Poo'},
        }

        expected = {
            "class_name": self.ivo_panda.__class__.__name__,
            "dict": dict_
        }

        self.assertEqual(ivo_panda_dict, json.dumps(expected, indent=4))

    def test_from_json_with_simple_data_tyupes(self):
        new_panda = Panda.from_json('''{
            "class_name": "Panda",
            "dict": {
            "name": "ivo",
            "age": 25
            }
        }''')
        # print(new_panda.__dict__)
        # print(self.ivo_panda.__dict__)
        self.assertEqual(new_panda.__dict__, self.ivo_panda.__dict__)

    def test_from_json_with_instance_of_other_class(self):
        new_panda = Panda.from_json("""{
            "class_name": "Panda",
            "dict": {
                "name": "ivo",
                "age": 25,
                "frend": {
                    "class_name": "Panda",
                    "dict": {
                        "name": "ivo",
                        "age": 25
                    }
                }
            }
        }""")
        expected_panda = self.ivo_panda
        expected_panda.frend = Panda()
        # print(new_panda.__dict__)
        # print(expected_panda.__dict__)
        self.assertEqual(new_panda, expected_panda)

    def test_from_json_for_value_error(self):
        # person = Person(name="Ico", age=30)
        # person_dict = person.to_json()
        # print(person_dict)
        # panda = Panda.from_json(person_dict)
        with self.assertRaises(ValueError):
            person = Person(name="Ico", age=30)
            person_dict = person.to_json()
            panda = Panda.from_json(person_dict)
        # print(person.__class__.__name__)
        # print(panda.__class__.__name__)
        # pass


if __name__ == "__main__":
    unittest.main()
