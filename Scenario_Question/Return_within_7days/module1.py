import datetime

def calc(cust_name, prod_name, purch_date):
    database = {'narendra': {'product_name': 'toy1', 'price': 499},
                'sujata': {'product_name': 'pink saree', 'price': 7500},
                'shritan': {'product_name':'t-shirt', 'price': 500}
                }

    if cust_name in database:
        if prod_name == database[cust_name]['product_name']:
            in_date_format_purch_date = datetime.datetime.strptime(purch_date, '%m/%d/%Y')
            if  datetime.datetime.today() < (in_date_format_purch_date + datetime.timedelta(days=7)):
                return f"{prod_name} will be collected from the delivered address and amount:{database[cust_name]['price']} will be returned to your account."
            else:
                return "Sorry! the product cannot be returned"
    else:
        return 'You have not purchased that product recently with us.'