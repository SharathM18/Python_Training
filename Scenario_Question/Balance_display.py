class Bank:
    def __init__(self):
        self.database = {
            100:{ 'name':'deepthi', 'pin': 1234, 'net balance':0},
            101:{ 'name':'eva', 'pin': 2345, 'net balance':100000},
            102:{ 'name':'raghavendra', 'pin': 3456, 'net balance':110000},
            103:{ 'name':'sthuthi', 'pin': 4567, 'net balance':85000},
            104:{ 'name':'sujay', 'pin': 5678, 'net balance':50500}
        }

    def calc(self):
        user_acc_number = int(input('Please enter your Account no.: '))
        if user_acc_number in self.database:
            user_acc_pin = int(input('Please enter the 4 digit pin: '))
            if user_acc_pin == self.database[user_acc_number]['pin']:
                print(f'Hi {self.database[user_acc_number]['name'].capitalize()}')
                print(f'Your net balance is: {self.database[user_acc_number]['net balance']}')
            else:
                print('Sorry Invalid Pin.')
        else:
            print('Entering wrong account no. Please try again.')
            print('Please visit our bank and create an account.')

Bank().calc()