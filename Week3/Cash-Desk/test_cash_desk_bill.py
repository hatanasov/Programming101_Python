import unittest
from cash_desk import Bill


class TestBill(unittest.TestCase):
    def setUp(self):
        self.my_bill = Bill(10)
        self.other_bill = Bill(10)
        self.third_bill = Bill(5)
        self.expected_str = 'A 10$ bill'

    def test_class_bill_negative_amount(self):
        with self.assertRaises(ValueError):
            self.negative = Bill(-10)

    def test_class_bill_not_int_amount(self):
        with self.assertRaises(TypeError):
            self.negative = Bill('10')

    def test_class_bill_int_dunder(self):
        self.assertEqual(int(self.my_bill), 10)

    def test_class_bill_str_dunder(self):
        self.assertEqual(str(self.my_bill), self.expected_str)

    def test_class_bill_print_dunder(self):
        self.assertEqual(self.my_bill.__repr__(), self.expected_str)

    def test_class_bill_eq_true_dunder(self):
        self.assertEqual(self.my_bill == self.other_bill, True)

    def test_class_bill_eq_false_dunder(self):
        self.assertEqual(self.my_bill == self.third_bill, False)


if __name__ == '__main__':
    unittest.main()
