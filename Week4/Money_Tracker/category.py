class Category:
    def __init__(self, category_name, data_dict):
        self.category_name = category_name
        self.data_dict = data_dict

    def get_data_from_category(self):
        result = {}
        for date in self.data_dict:
            result[date] = []
            if self.category_name in self.data_dict[date]:
                for category in self.data_dict[date][self.category_name]:
                    result[date].append(category)
        return result

    @classmethod
    def add_category(cls, date_as_string, cat_name, data_dict):
        # day, month, year = date_as_string.split('-')
        category = cls(cat_name, data_dict)
        if cls.date_is_valid(date_as_string):
            if date_as_string not in category.data_dict:
                # category.data_dict.update({date_as_string: {cat_name: []}})
                category.data_dict[date_as_string] = {cat_name: []}
            elif cat_name not in category.data_dict[date_as_string]:
                category.data_dict[date_as_string][cat_name] = []
        return category.data_dict

    @staticmethod
    def date_is_valid(date_as_string):
        from datetime import date
        day, month, year = map(int, date_as_string.split('-'))
        try:
            chech_date = date(year, month, day)
            return chech_date
        except ValueError:
            print('The date is not valid!')


