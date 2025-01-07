class Bank:
    def __init__(self):
        self.name = None
        self.acc_no = None
        self.initial_balance = 0
        self.data = {}

    def user_account_details(self):
        self.name = input('Enter the name: ')
        self.acc_no = int(input('Enter the account: '))
        self.initial_balance = float(input('Initial Deposit amount: '))

        self.data[self.acc_no] = {'name': self.name, 'acc_no': self.acc_no, 'balance': self.initial_balance}

    def deposit(self):
        acc_no_for_deposit = int(input('Enter the account number: '))

        if acc_no_for_deposit in self.data:

            while True:
                self.amount_for_deposit = float(input('Enter the amount: '))

                if self.amount_for_deposit < 0:
                    print("We can't deposit -ve amount. Retry.....")
                else:
                    self.data[acc_no_for_deposit]['balance'] += self.amount_for_deposit
                    break

        else:
            print('invalid account number')

    def withdrawal(self):
        acc_no_for_wd = int(input('Enter the account number: '))

        if acc_no_for_wd in self.data:
            if self.data[acc_no_for_wd]['balance'] == 0:
                print('Balance is 0')

            elif self.data[acc_no_for_wd]['balance'] > 0:
                amount_for_wd = float(input('Enter the amount for withdrawal: '))

                if self.data[acc_no_for_wd]['balance'] < amount_for_wd:
                    print('insufficient amount')
                    return

                self.data[acc_no_for_wd]['balance'] -= amount_for_wd

            else:
                print('insufficient amount')
        else:
            print('invalid account number')

    def balance(self):
        acc_no_for_b = int(input('Enter the account number: '))

        if acc_no_for_b in self.data:
            print(f'Balance: {self.data[acc_no_for_b]['balance']}')
        else:
            print('invalid account number')

    def menu(self):
        menu_display = True

        while menu_display:
            print('1. Account Creation')
            print('2. deposit')
            print('3. withdrawal')
            print('4. balance')
            print('5. exit')
            choice = int(input('Choose option one at a time: '))
            match choice:
                case 1:
                    self.user_account_details()
                case 2:
                    self.deposit()
                case 3:
                    self.withdrawal()
                case 4:
                    self.balance()
                case 5:
                    print('see you soon....')
                    menu_display = False
                case _:
                    print('invalid options')
                    self.menu()

bank = Bank()
bank.menu()