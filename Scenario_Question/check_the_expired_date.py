import datetime

data = {
    1: {"name": "Soap", "best_before": 12, "manufactured_date": "01-02-2024"},
    2: {"name": "Shampoo", "best_before": 6, "manufactured_date": "03-14-2024"},
    3: {"name": "Toothpaste", "best_before": 7, "manufactured_date": "02-12-2024"},
    4: {"name": "Ready juice", "best_before": 2, "manufactured_date": "11-08-2024"},
    5: {"name": "Chips", "best_before": 5, "manufactured_date": "11-20-2024"},
}

def abc_super_market(prod_code, data):
    for k, v in data.items():
        if k == prod_code:

            manu_date = datetime.datetime.strptime(v['manufactured_date'], "%m-%d-%Y")
            expiry_date =manu_date  + datetime.timedelta(days= v['best_before'] * 30)
            today_date = datetime.datetime.today()

            if today_date > expiry_date:
                print(f"The product '{v['name']}' is expired.")
            else:
                print(f"The product '{v['name']}' can be kept on shelves.")


prod_code = int(input('Enter the product code: '))
abc_super_market(prod_code, data)

