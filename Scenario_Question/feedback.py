import json

class Feedback:
    def __init__(self):
        self.customer_name = ""
        self.product_name = ""
        self.user_feedback = ""

    def save_data(self, data, file_name):
        with open(f'{file_name}.json', 'w') as file:
            json.dump(data, file, indent=4)

    def user_ip(self):
        self.customer_name = input('Customer name: ')
        self.product_name = input('Product name: ')
        self.user_feedback = input('Feedback: ')

        self.save_data({'name': self.customer_name, 'product name':self. product_name, 'user feedback': self.user_feedback}, self.customer_name)

        print('Thanks for feedback...')


Feedback().user_ip()