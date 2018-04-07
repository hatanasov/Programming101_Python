def list_user_data():
    with open('money_tracker.txt', 'r') as f_read:
        content = f_read.read()
        cont_list = [line for line in content.split('\n') if line]
        return cont_list


data_list = list_user_data()
# print(data_list)


def user_data(user_data_string):
    assert type(user_data_string) is list
    result = {}
    dates = [d for date in user_data_string if '=' in date for d in date.split(' ') if '=' not in d]
    # print(dates)
    flag = ''
    for date in dates:
        for line in user_data_string:
            if flag == 'stop':
                break
            elif date in line:
                flag = 'start'
            elif flag == 'start' and '=' not in line:
                if date not in result:
                    result[date] = [line.split(', ')]
                else:
                    result[date].append(line.split(', '))
            elif flag == 'start' and '=' in line:
                flag = 'stop'
        flag = ''

    return result


data_dict = user_data(data_list)
print(data_dict)


def show_user_savings(data_dict):
    result = []
    for values in data_dict.values():
        for line in values:
            if 'Salary' in line or 'Savings' in line or 'Deposit' in line:
                saving = [elements for elements in line]
                try:
                    money = int(saving[0])
                    if money > 0:
                        result.append((money, saving[1]))
                except ValueError:
                    money = float(saving[0])
                    result.append((money, saving[1]))
    # result = sorted(result, key=lambda x: x[1])
    return result



def show_user_deposits():
    pass


def show_user_expenses():
    pass


def list_user_expenses_ordered_by_categories():
    pass


def show_user_data_per_date(wanted_date, data_dict):
    from datetime import date
    check_date = wanted_date.split('-')
    year = int(check_date[2])
    month = int(check_date[1])
    day = int(check_date[0])
    result = []
    try:
        date(year, month, day)
        for orders in data_dict[wanted_date]:
            result.append((orders[0], orders[1], orders[2]))
    except ValueError:
        print('The date is not valid')
        return
    except KeyError:
        print('No records for {}'.format(wanted_date))
        return

    # result = []
    # try:
    #     for orders in data_dict[wanted_date]:
    #         result.append((orders[0], orders[1], orders[2]))
    # except KeyError:
    #     print('No records for {}'.format(wanted_date))
    return result


print(show_user_data_per_date('40-03-2018', data_dict))


def list_income_categories():
    pass


def list_expense_categories():
    pass


def add_income(income_category, money, date):
    pass


def add_expense(expense_category, money, date):
    pass
