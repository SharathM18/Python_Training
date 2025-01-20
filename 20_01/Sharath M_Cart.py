from abc import ABC, abstractmethod

class Cart(ABC):
    def __init__(self):
        self._database = {'sugar': 50,'rice':55, 'wheat flour':55, 'toor dal': 150, 'rava':70 }

    @abstractmethod
    def calc(self):
        pass

class Store(Cart):
    def calc(self):
        print('Product:Price in Rs.')
        for prod_name, price in self._database.items():
            print(f'{prod_name}: {price}')

        user_prod_name = input('Enter the item name to add it to the cart: ').lower()

        if user_prod_name in self._database:
            user_quantity = int(input('Enter the quantity in Kgs:'))
            if user_quantity == 0:
                print('Thank you')
                exit()

            print('Cart:')
            print('Product: Quantity: Price in Rs.')
            print(f'{user_prod_name.capitalize()}: {user_quantity}: {user_quantity * self._database[user_prod_name]}')
            print('Thank you')

        else:
            print("Please enter the existing product's name in the list")

Store().calc()





