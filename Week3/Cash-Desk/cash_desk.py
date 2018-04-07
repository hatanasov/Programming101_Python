class Bill:
    def __init__(self, amount):
        self.amount = amount
        if self.amount < 0:
            raise ValueError
        elif type(self.amount) != int:
            raise TypeError

    def __int__(self):
        return self.amount

    def __str__(self):
        return 'A {}$ bill'.format(self.amount)

    def __repr__(self):
        return 'A {}$ bill'.format(self.amount)

    def __eq__(self, other):
        if self.amount == other:
            return True
        else:
            return False

    def __hash__(self):
        return self.amount


class BatchBill:
    def __init__(self, list_bills):
        self.list_bills = list_bills

    def __len__(self):
        count = 0
        for n in self.list_bills:
            count += 1
        return count

    def total(self):
        total = 0
        for bill in self.list_bills:
            total += bill.amount
        return total

    def __getitem__(self, index):
        return self.list_bills[index]


class CashDesk:
    def __init__(self):
        self.total_amount = 0
        self.bills = {}

    def sum_total(self, bill):
        self.total_amount += bill.amount
        if bill not in self.bills:
            self.bills[bill] = 1
        else:
            self.bills[bill] += 1

    def take_money(self, money):
        if type(money) == Bill:
            self.sum_total(money)
        else:
            for bill in money:
                self.sum_total(bill)
        return self.total_amount

    def total(self):
        return self.total_amount

    def inspect(self):
        print_total = 'We have a total of {}$ in the desk\n'.format(self.total_amount)
        print_next = 'We have the following count of bills, sorted in ascending order:\n'
        print_bills = ''
        for key, value in self.bills.items():
            print_bills += '{} - {}\n'.format(key, value)
        result = print_total + print_next + print_bills
        return result
