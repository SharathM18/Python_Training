database = {
    'bengaluru': 560062,
    'mandya': 571401,
    'hyderabad': 500081
}

def check_location(city, database):
    for key, value in database.items():
        if city == key or city == str(value):
            print('quick delivery possible')
            break
    else:
        print('sorry, quick delivery possible')


city = input('Enter the full address: ')
check_location(city, database)