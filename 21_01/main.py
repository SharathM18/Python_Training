# package, file handling, json dump
# zip and unzip files, csv retrieve and load

from my_package import mod1
print(mod1.greeting())

import calendar
print(calendar.monthcalendar(2025,1))
print(calendar.MONDAY, calendar.TUESDAY) # 0 1

with open('demo.txt','a') as file:
    file.write('append text ')

with open('demo.txt', 'r') as file:
    print(file.read())

print('the lion king'.title()) # The Lion King