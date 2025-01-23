class XYZ:
    def __init__(self):
        self.res_amount = 0
        self.prod_price = {
            'sugar': 50,
            'rice': 55,
            'wheat flour': 55,
            'toor dal': 150,
            'rava': 70
        }

    def greeting(self):
        print('Welcome to our shop.The list items:')
        print('Product:Price in Rs. \nRava:70 \nRice:55 \nSugar:50 \nToor dal:150 \nWheat flour:55')
        print('For your surprise we have offers going on: \nBuy 2 KGs Sugar and get 50% off and flat 50% off on Wheat flour.')
        self.calc()

        
    def calc(self):
        prod_name = input('Enter the item name: ').lower()

        match prod_name:
            case 'rava':
                quantity = int(input(f'Enter the Quantity of {prod_name}: '))
                rava_amt = quantity * self.prod_price['rava']
                self.res_amount += rava_amt

            case 'rice':
                quantity = int(input(f'Enter the Quantity of {prod_name}: '))
                rice_amt = quantity * self.prod_price['rice']
                self.res_amount += rice_amt

            case 'sugar':
                quantity = int(input(f'Enter the Quantity of {prod_name}: '))
                if quantity < 2:
                    sugar_amt = quantity * self.prod_price['sugar']
                    self.res_amount += sugar_amt
                elif quantity >= 2:
                    two_kg = (quantity // 2) * self.prod_price['sugar']
                    remaining_kg = (quantity % 2) * self.prod_price['sugar']
                    sugar_amt = two_kg + remaining_kg
                    self.res_amount += sugar_amt

            case 'toor dal':
                quantity = int(input(f'Enter the Quantity of {prod_name}: '))
                dal_amt = quantity * self.prod_price['toor dal']
                self.res_amount += dal_amt

            case 'wheat flour':
                quantity = int(input(f'Enter the TQuantity of {prod_name}: '))
                wheat_amt = (quantity * self.prod_price['wheat flour']) / 2
                self.res_amount += wheat_amt

            case _:
                print('Enter the item name present in our shop and try again.')
                self.calc()

        is_anything_else = input('is there anything else (y/n): ')
        if is_anything_else == 'y':
            self.calc()
        else:
            print(f'Please pay Rs.: {self.res_amount}')
            exit()

obj = XYZ()
obj.greeting()