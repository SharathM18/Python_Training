database = {
    'pdcc01': {'name': 'chair', 'price': 1500, 'location': 'B1R1C2', 'quantity': 2},
    'pdcs11': {'name': 'sofa',  'price': 50000, 'location': 'B2R4C1', 'quantity': 1},
    'pdct25': {'name': 'table',  'price': 15000, 'location': 'B3R3C2', 'quantity': 1},
    'pdcd011': {'name': 'desk',  'price': 900, 'location': 'B4R2C3', 'quantity': 13},
    'pdcR012': {'name': 'shelf',  'price': 2500, 'location': 'B5R1C4', 'quantity': 0}
}

def funiture(prod_code, database):
    if prod_code not in database:
        print('Please enter a valid product code.')
        exit()

    if database[prod_code]['quantity'] <= 0:
        print('Sorry! Out of stock')
        exit()

    if prod_code in database:
        ip_prod_type = input('Product Type: ')
        if ip_prod_type == 'sofa' or  'table':
            print(f'product price: {database[prod_code]['price']} + 600/- Rs. Delivery charge.')
            print(f'Please pay Rs. {database[prod_code]['price'] + 600} ')
            print('The product will be delivered to your home.')
        else:
            print(f'product price: {database[prod_code]['price']}')
            print(f'You can collect the product in the ground floor, {database[prod_code]['location']}')

ip_product_code = input('Please enter the product code: ')
funiture(ip_product_code, database)