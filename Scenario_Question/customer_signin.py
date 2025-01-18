import re

class Customer:
    def __init__(self):
        self.full_name  = ""
        self.address = []
        self.email = ""
        self.card_number = ""
        self.gst_number = ""

    def greeting(self):
        print('Please fill the details to sign in.')
        self.ip_full_name()

    def ip_full_name(self):
        while True:
            self.full_name = input("full name: ")
            if len(self.full_name) >= 3:
                break
            print("invalid name")

        self.ip_email()

    def ip_email(self):
        while True:
            self.email = input("email: ")
            if re.match(r'^[^@]+@[^@]+\.[^@]+$', self.email):
                break
            print("invalid email")

        self.ip_address()

    def ip_address(self):
        while True:
            print("address:")
            self.address = [
                input("line 1: "),
                input("line 2: "),
                input("line 3: ")
            ]

            if all(self.address):
                break
            print("address is empty.")

        self.ip_card_number()

    def ip_card_number(self):
        while True:
            self.card_number = int(input("card number: "))
            if len(str(self.card_number)) == 16:
                break
            print("card number length should be 16")

        self.ip_gst_number()

    def ip_gst_number(self):
        while True:
            self.gst_number = input("gst number: ")
            if re.match(r'^\d{8}[A-Za-z]{7}$', self.gst_number):
                break
            print("invalid gst number")

        self.display()

    def display(self):
        print('user details \n')
        print(f'full name: {self.full_name}')
        print(f'email: {self.email}')
        for i, j in enumerate(self.address):
            print(f'Line {i}: {j}')
        print(f'card number: {self.card_number}')
        print(f'gst number: {self.gst_number}')
        print('\nThank you.')

Customer().greeting()