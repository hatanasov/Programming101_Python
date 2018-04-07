import unittest
from cash_desk import BatchBill
from cash_desk import Bill


class TestBatchBill(unittest.TestCase):
    def setUp(self):
        self.list_values = [10, 20, 30]
        self.bill = [Bill(value) for value in self.list_values]
        self.Bbill = BatchBill(self.bill)

    def test_len(self):
        self.assertEqual(self.Bbill.__len__(), 3)

    def test_total(self):
        self.assertEqual(self.Bbill.total(), 60)


if __name__ == '__main__':
    unittest.main()
