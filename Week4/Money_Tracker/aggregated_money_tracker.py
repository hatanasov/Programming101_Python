class AggregatedMoneyTracker:
    def __init__(self, data_list):
        self.data_list = data_list

    def _dict_data(self):
        dates = [d for date in self.data_list if '=' in date for d in date.split(' ') if '=' not in d]
        result = {}
        flag = ''
        for date in dates:
            for line in self.data_list:
                if flag == 'stop':
                    break
                elif date in line:
                    flag = 'start'
                elif flag == 'start' and '=' not in line:
                    if date not in result:
                        result[date] = [line]
                    else:
                        result[date].append(line)
                elif flag == 'start' and '=' in line:
                    flag = 'stop'
            flag = ''

        return result

    def aggregate_data(self):
        data = self._dict_data()
        agr_data = {}
        income = 'income'
        expense = 'expense'
        for date in data:
            agr_data[date] = {'income': [], 'expense': []}
            for line in data[date]:
                if 'New Income' in line:
                    agr_data[date][income].append(line)
                elif 'New Expense' in line:
                    agr_data[date][expense].append(line)
        return agr_data
