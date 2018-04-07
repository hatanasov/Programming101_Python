import unittest
import coding_skils


class TestCodingSkils(unittest.TestCase):

    def setUp(self):
        self.work_file = 'data.json' ### DOnt test with file !!!
        self.data_dict = {'people': [{'first_name': 'Ivo', 'last_name': 'Ivo',
                                      'skills': [{'name': 'C++', 'level': 30}, {'name': 'PHP', 'level': 25}]},
                                     {'first_name': 'Rado', 'last_name': 'Rado',
                                      'skills': [{'name': 'C++', 'level': 20}, {'name': 'PHP', 'level': 37}]},
                                     {'first_name': 'Pavli', 'last_name': 'Pavli',
                                      'skills': [{'name': 'Python', 'level': 77}]}]}

        self.data_dict_simple = {'people': [{'first_name': 'Ivo', 'last_name': 'Ivo',
                                             'skills': [{'name': 'C++', 'level': 30}]},
                                            {'first_name': 'Rado', 'last_name': 'Rado',
                                             'skills': [{'name': 'C#', 'level': 20}]},
                                            {'first_name': 'Pavli', 'last_name': 'Pavli',
                                             'skills': [{'name': 'Python', 'level': 77}]}]}

        self.simpe_result = [{'C++': 'Ivo Ivo'}, {'C#': 'Rado Rado'}, {'Pavli Pavli': 'Python'}]

        self.result = [{'C++': 'Ivo Ivo'}, {'PHP': 'Rado Rado'}, {'Pavli Pavli': 'Python'}]

        self.person_info = {'first_name': 'Ivo', 'last_name': 'Ivo',
                            'skills': [{'name': 'C++', 'level': 30},
                                       {'name': 'PHP', 'level': 25},
                                       {'name': 'Python', 'level': 80},
                                       {'name': 'C#', 'level': 25}]}

    def test_coding_skils_no_data(self):
        self.assertEqual(coding_skils.coding_skils({}), '')

    def test_coding_skipls_simle(self):
        self.assertEqual(coding_skils.coding_skils(self.data_dict_simple), self.simpe_result)

    def test_coding_skils(self):
        self.assertEqual(coding_skils.coding_skils(self.data_dict), self.result)




if __name__ == '__main__':
    unittest.main()
