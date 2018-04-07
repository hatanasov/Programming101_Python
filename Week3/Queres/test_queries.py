import unittest
import queries


class TestQueries(unittest.TestCase):

    def setUp(self):
        self.data = [{'full_name': 'Michael Olson', 'favourite_color': 'olive', 'company_name': 'Scott, Young and King',
                      'email': 'zacharymcdonald@yahoo.com', 'phone_number': '114-116-1124x315', 'salary': '2500'},
                     {'full_name': 'Diana Harris', 'favourite_color': 'lime', 'company_name': 'Martin-Barnes',
                      'email': 'timothy81@gmail.com', 'phone_number': '1-860-251-9980x6941', 'salary': '5354'},
                     {'full_name': 'Marilyn Maldonado', 'favourite_color': 'black', 'company_name': 'Walker PLC',
                      'email': 'gmcintosh@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '7158'},
                     {'full_name': 'Hristo Atanasov', 'favourite_color': 'black', 'company_name': 'Mtel',
                      'email': 'hatanasov@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '2100'}]

    def test_filter_by_one_arg(self):
        self.assertEqual(
            queries.filter_by(self.data, full_name='Marilyn Maldonado'),
            [{'full_name': 'Marilyn Maldonado', 'favourite_color': 'black', 'company_name': 'Walker PLC',
              'email': 'gmcintosh@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '7158'}])

    def test_filter_by_two_args(self):
        self.assertEqual(
            queries.filter_by(self.data, favourite_color='black', full_name='Hristo Atanasov'),
            [{'full_name': 'Hristo Atanasov', 'favourite_color': 'black', 'company_name': 'Mtel',
              'email': 'hatanasov@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '2100'}])


    def test_filter_startswith(self):
        self.assertEqual(
            queries.startswith(self.data, full_name__startswith='Michael'),
            [{'full_name': 'Michael Olson', 'favourite_color': 'olive', 'company_name': 'Scott, Young and King',
              'email': 'zacharymcdonald@yahoo.com', 'phone_number': '114-116-1124x315', 'salary': '2500'}])

    def test_contains(self):
        self.assertEqual(
            queries.contains(self.data, email__contains="@gmail"),
            [{'full_name': 'Diana Harris', 'favourite_color': 'lime', 'company_name': 'Martin-Barnes',
              'email': 'timothy81@gmail.com', 'phone_number': '1-860-251-9980x6941', 'salary': '5354'}])

    def test_interval_search(self):
        self.assertEqual(
            queries.interval_search(self.data, salary__gt=1000, salary__lt=3000),
            [{'full_name': 'Michael Olson', 'favourite_color': 'olive', 'company_name': 'Scott, Young and King',
              'email': 'zacharymcdonald@yahoo.com', 'phone_number': '114-116-1124x315', 'salary': '2500'},
             {'full_name': 'Hristo Atanasov', 'favourite_color': 'black', 'company_name': 'Mtel',
              'email': 'hatanasov@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '2100'}])

    def test_interval_search_ordered(self):
        self.assertEqual(
            queries.interval_search_ordered(self.data, salary__gt=1000, salary__lt=3000, order_by='salary'),
        [{'full_name': 'Hristo Atanasov', 'favourite_color': 'black', 'company_name': 'Mtel',
          'email': 'hatanasov@yahoo.com', 'phone_number': '+49(1)7897611670', 'salary': '2100'},
         {'full_name': 'Michael Olson', 'favourite_color': 'olive', 'company_name': 'Scott, Young and King',
          'email': 'zacharymcdonald@yahoo.com', 'phone_number': '114-116-1124x315', 'salary': '2500'}])
