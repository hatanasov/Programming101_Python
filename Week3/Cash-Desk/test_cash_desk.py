import unittest
from cash_desk import *


class TestCashDesk(unittest.TestCase):
    def setUp(self):
        self.bill = Bill(10)
        self.bill2 = Bill(20)
        self.BB = BatchBill([self.bill, self.bill2])
        self.cashe = CashDesk()

    def test_take_money_bill(self):
        self.assertEqual(self.cashe.take_money(self.bill),  10)

    def test_take_money_batchbill(self):
        self.assertEqual(self.cashe.take_money(self.BB), 30)

