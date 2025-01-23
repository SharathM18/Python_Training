'''
Assignment:
1. Write a program to raise exception
a. enter name of the person raise exception where it is below 3 letters
b. enter salary of the person raise exception when salary below 10000

2. Define your exception as UsernameLengthFailure
a. enter username if namelength is below 4 and above 8 raise exception
'''

try:
    if len(input('enter name of the person: ')) < 3:
        raise 'name must be > 3'

    if float(input('enter salary of the person: ')) < 10000:
        raise 'salary must be > 10000'
except:
    print('Error')

