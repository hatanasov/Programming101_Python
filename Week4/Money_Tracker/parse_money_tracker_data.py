class MoneyTrackerData:
    def __init__(self, filename):
        self.filename = filename

    def list_user_data(self):
        with open(self.filename, 'r') as f_read:
            content = f_read.read()
            cont_list = [line for line in content.split('\n') if line]
            return cont_list
