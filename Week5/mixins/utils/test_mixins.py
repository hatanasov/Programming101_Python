import unittest
from serializers import Jsonable
import json

class Frends(Jsonable):
    def __init__(self):
        self.name = 'Poo'

class Panda(Jsonable):
    def __init__(self ):
        self.name = 'ivo'
        self.age = 25
        self.food = ['bambuk', 'mint']



class TestJsonable(unittest.TestCase):
    def setUp(self):
        self.ivo_panda = Panda()
        self.ivo_panda_dict = self.ivo_panda.to_json()
        self.expexted = {
            "class_name": self.ivo_panda.__class__.__name__,
            "dict": self.ivo_panda.__dict__
        }

    def test_to_json(self):
        self.assertEqual(self.ivo_panda_dict, json.dumps(self.expexted, indent=4))

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



if __name__ == "__main__":
    unittest.main()