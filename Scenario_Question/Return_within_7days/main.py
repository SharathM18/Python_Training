import module1

print('Please enter the details to return the product.')
name = input('Enter your name: ').lower()
prod_name = input('Enter the product name: ').lower()
print('When did you purchase the product?')
purchased_date = input('Please enter the date in mm/dd/yyyy format: ')
print(module1.calc(name, prod_name, purchased_date))
print('Thank you.')