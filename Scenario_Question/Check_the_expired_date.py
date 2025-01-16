import datetime

print(datetime.date(2020, 5, 17) + datetime.timedelta(10))
# data = {
#     1: {"name": "Soap", "best_before": 12, "manufactured_date": "01-02-22"},
#     2: {"name": "Shampoo", "best_before": 6, "manufactured_date": "03-14-22"},
#     3: {"name": "Toothpaste", "best_before": 7, "manufactured_date": "02-12-22"},
#     4: {"name": "Ready juice", "best_before": 2, "manufactured_date": "11-08-22"},
#     5: {"name": "Chips", "best_before": 1, "manufactured_date": "11-20-22"},
# }
# def abc_super_market(prod_code, data):
#     if data['product_code'] != prod_code:
#
#         exit()
#
#     else:
#         expiry_date = data['manufactured_date'] + timedelta(days= best_month * 30)
#         today_date = datetime.date.today()
#
#         if expiry_date < today_date:
#             print(f"The product '{data['product_name']}' is expired.")
#         else:
#             print(f"The product '{data['product_name']}' can be kept on shelves.")
#
#
# prod_code = int(input('Enter the product code: '))
# abc_super_market(prod_code, data)