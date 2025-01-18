database = {
    "sajid": 120,
    "roopesh": 85,
    "koushik": 50,
    "lakshmi": 64,
    "sathvik": 12
}

class loyalty_points:
    def __init__(self, database):
        self.database = database
        self.coupon_code = "123476"

    def calc(self):
        ip_name = input('Please enter the customer name: ').lower()
        if ip_name not in self.database:
            print('new customer')

        amount = int(input('Enter the bill amount to be paid: '))
        if ip_name not in self.database:
            self.database[ip_name] = amount // 100
        else:
            self.database[ip_name] += amount // 100

        coupon = input('Do the customer has the coupon? Type y or n: ').lower()

        if coupon == 'y':
            if self.coupon_code == input('Please enter the coupon code: '):
                self.database[ip_name] += 20
                if self.database[ip_name] >= 100:
                    print(f'Congratulations! you won Rs. 100 cash back. You have to pay Rs.: {amount - 100} Thank you.')
                    print(f'And remaining loyalty points in your account is: {self.database[ip_name] - 100}')
                else:
                    print(f'You have {self.database[ip_name]} loyalty points in your account. Please pay Rs.: {amount} Thank you.')
            else:
                print(f'invalid coupon')
                print(f'You have {self.database[ip_name]} loyalty points in your account. Please pay Rs.: {self.database[ip_name]} Thank you.')

        else:
            if self.database[ip_name] >= 100:
                print(f'Congratulations! you won Rs. 100 cash back. You have to pay Rs.: {amount - 100} Thank you.')
                print(f'And remaining loyalty points in your account is: {self.database[ip_name] - 100}')

            else:
                print(f'You have {self.database[ip_name]} loyalty points in your account. Please pay Rs.: {amount} Thank you.')


loyalty_points(database).calc()