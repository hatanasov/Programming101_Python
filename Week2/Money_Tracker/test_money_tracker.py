import unittest
import money_tracker


class TestMoneyTracker(unittest.TestCase):
    def setUp(self):
        self.data_list = ['=== 22-03-2018 ===', '760, Salary, New Income',
                          '=== 24-03-2018 ===', '50, Savings, New Income',
                          '=== 23-03-2018 ===', '200, Deposit, New Income']

        self.data_dict = {'22-03-2018': [['760', 'Salary', 'New Income']],
                          '24-03-2018': [['50', 'Savings', 'New Income']],
                          '23-03-2018': [['200', 'Deposit', 'New Income']]}

    def test_user_data_no_data(self):
        self.assertEqual(money_tracker.user_data([]), {})

    def test_user_data(self):
        self.assertEqual(money_tracker.user_data(self.data_list), self.data_dict)

    def test_user_data_inislist(self):
        with self.assertRaises(AssertionError):
            money_tracker.user_data({})

    # def test_list_user_data(self):
    #     self.assertEqual(money_tracker.list_user_data(), self.file_contetnt())
    #
    def test_show_user_savings(self):
        self.assertEqual(money_tracker.show_user_savings(self.data_dict),
                         [(760, 'Salary'), (50, 'Savings'), (200, 'Deposit')])
    #
    # def test_list_user_expenses_ordered_by_categories(self):
    #     self.assertEqual(money_tracker.list_user_expenses_ordered_by_categories(),
    #                      [(112.40, 'Bills'), (34, 'Clothes'), (5.5, 'Eating Out'),
    #                       (12, 'Eating Out'), (15, 'Food'), (41.79, 'Food'), (7, 'House'),
    #                       (14, 'Pets'), (5, 'Sports'), (21.5, 'Transport')])
    #

    def test_show_user_data_per_date(self):
        self.assertEqual(money_tracker.show_user_data_per_date('23-03-2018', self.data_dict),
                         [('200', 'Deposit', 'New Income')])

    def test_show_user_data_per_no_date(self):
        self.assertEqual(money_tracker.show_user_data_per_date('26-03-2018', self.data_dict),
                         [])

    def test_test_show_user_data_per_fake_date(self):
        self.assertEqual(money_tracker.show_user_data_per_date('40-03-2018', self.data_dict),
                         None)


if __name__ == '__main__':
    unittest.main()
