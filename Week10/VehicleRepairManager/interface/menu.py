import sys
from controller.controller import Controller
from interface.settings import *


class Menu:
    """All messages are stored in interface.settings module"""

    def start(self):
        self.user_name = input(welcome_msg + request_username)

        if not Controller().check_user_name(self.user_name):
            reg_user = input(unknown_user_msg)
            if reg_user.lower() in yes:
                self.request_user_data()
            else:
                print(goodbye)
                sys.exit()

        else:
            self.user_servise()

    def user_servise(self):
        print(welcome_to_service)
        client_choice = input(menu_options)
        print(client_choice)

    def request_user_data(self):
        # user_name = None
        user_data = {}
        confirm = input('{} "{}" {} === '.format(
            confirm_username, self.user_name, y_or_n))
        if confirm.lower() in yes:
            user_data['user_name'] = self.user_name
        else:
            self.user_name = input(request_username)
        self.user_type = input(client_or_mechanic)
        user_data['user_type'] = self.user_type
        self.email = input(request_email_msg)
        if self.email:
            user_data['email'] = self.email
        else:
            user_data['email'] = None
        self.phone_number = input(request_phone_number_msg)
        user_data['phone_number'] = self.phone_number
        self.address = input(request_address)
        if self.address:
            user_data['address'] = self.address
        else:
            user_data['address'] = None
        is_user_data_valid = Controller().validate_user_data(user_data)
        if is_user_data_valid:
            Controller().registrate_user(user_data)
            self.user_servise()
        else:
            print(no_valid_user_data)
            again = input(again_msg)
            if again.lower() in yes:
                self.request_user_data()
            else:
                print(goodbye)
                sys.exit()
