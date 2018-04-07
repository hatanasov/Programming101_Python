from parse_money_tracker_data import MoneyTrackerData
from aggregated_money_tracker import AggregatedMoneyTracker
from category import Category

data_obj = MoneyTrackerData('money_tracker.txt')
data_list = data_obj.list_user_data()
# print(data_list)
agr_data = AggregatedMoneyTracker(data_list)
agr_dict = agr_data.aggregate_data()
# print(agr_data._dict_data())
print(agr_dict)
income = Category('income', agr_dict)
# print(income.get_data_from_category())
income.add_category('31-03-2018', 'income', agr_dict)
income.add_category('31-03-2018', 'expense', agr_dict)
income.add_category('30-03-2018', 'expense', agr_dict)
print(income.get_data_from_category())
print(agr_dict)
