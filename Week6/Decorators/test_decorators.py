import unittest
from decorators import accepts
from decorators import encrypt

class TestDecorators(unittest.TestCase):
    
    def test_accept_decorator(self):

        @accepts(str)
        def print_something(string):
            return string

        @accepts(str, int)
        def print_all_elements(name, salary):
            return {name: salary}

        with self.subTest("Test decorator with string"):
            self.assertEqual(print_something("Ico"), "Ico")

        with self.subTest("Test assertion error"):
            with self.assertRaises(TypeError):
                print_something(10)

        with self.subTest("Test accepts decorator with a few diferent type elements."):
            self.assertEqual(print_all_elements("Ico", 2000), {"Ico":2000})


        with self.subTest("Test accepts decorator with a few diferent type elements, one is wrong"):
            with self.assertRaises(TypeError):
                print_all_elements("ico", [100, 200])

    def test_encrypt_decorator(self):
        @encrypt(2)
        def get_low():
            return "Get get get low"
        self.assertEqual(get_low(), "Igv igv igv nqy")




if __name__ == "__main__":
    unittest.main()