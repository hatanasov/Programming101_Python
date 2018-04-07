import unittest
from coding_skils_2 import person_data


class TestCodingSkills2(unittest.TestCase):
    def test_person_data(self):
        data_dict = {'people': [{'first_name': 'Ivo', 'last_name': 'Ivo',
                      'skills': [{'name': 'C++', 'level': 30}, {'name': 'PHP', 'level': 25}]},
                     {'first_name': 'Rado', 'last_name': 'Rado',
                      'skills': [{'name': 'C++', 'level': 20}, {'name': 'PHP', 'level': 37}]},
                     {'first_name': 'Magi', 'last_name': 'Magi',
                      'skills': [{'name': 'JavaScript', 'level': 62}, {'name': 'Python', 'level': 66}]}]}
        skills_dict = {'C++': ['Ivo Ivo', 30], 'PHP': ['Rado Rado', 37], 'JavaScript': ['Magi Magi', 62],
                       'Python': ['Magi Magi', 66]}
        self.assertEqual(person_data(data_dict), skills_dict)


if __name__ == '__main__':
    unittest.main()
