'''
Assignment:
1. Write a program to raise exception
a. enter name of the person raise exception where it is below 3 letters
b. enter salary of the person raise exception when salary below 10000

2. Define your exception as UsernameLengthFailure
a. enter username if namelength is below 4 and above 8 raise exception
'''

class UsernameLengthFailure(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CustomError: {self.message}"


try:
    if len(input('enter name of the person: ')) < 3:
        raise UsernameLengthFailure('name must be > 3')

    if float(input('enter salary of the person: ')) < 10000:
        raise UsernameLengthFailure('salary must be > 10000')

    user_ip = len(input('enter username of the person: '))

    if not user_ip > 3 and user_ip < 8:
        raise UsernameLengthFailure('Username Length Failure')

except UsernameLengthFailure as e:
    print(e)

