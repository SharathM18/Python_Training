# regular expression - match, search, sub, findall,
import os
import re
from calendar import month

result = re.match(r'TSE', 'TSE offers Python training at Madhapur')
print(result)
print(result.group(0))
print(result.start())
print(result.end())

# s=input("Enter pattern to check: ")
# m=re.fullmatch(s,"ababab")
# print(m) # None or <re.Match object; span=(0, 6), match='ababab'>
# if m!= None:
#     print("Full String Matched")
# else:
#     print("Full String not Matched")

result = re.search(r'at', 'TSE offers Python training at Madhapur')
print(result.group(0),result.start(),result.end())

result = re.findall(r'TSE', 'TSE offers Python training at Madhapur ') # return list
print(result)
l=re.findall("[0-9]","a7b9c5kz") # ['7', '9', '5']
print(l)
a=re.findall("[a-z]","a7b9c5kz") # ['a', 'b', 'c', 'k', 'z']
print(a)

email=re.split(r'\.',"www.tse.com")
print(email) # ['www', 'tse', 'com']

num = '123456789'
# print('match : ', len(re.findall('\d', num))) # 9

# math module

import math
print(math.ceil(-32.1))
print(math.ceil(5.1))
print(math.ceil(5.9))

c=7.1
print(c.__ceil__())

import math
print(math.floor(7))
print(math.floor(7.9))
print(math.floor(7.1))
print(math.floor(-0.5)) #=-1
c=444
print(c.__floor__())

print(math.fabs(-8.9)) # 8.9

print(math.factorial(5))

print(math.gcd(3,13))
print(math.lcm(3,13))

a=[0.1,0.1,0.1,0.1,0.1,0.1,0.1,0.1]
print(math.fsum(a))
print(sum(a))

print(round(2.5), round(3.5)) # even number retain 2 and odd number next number

# sys module

import sys
sys.stdout.write('deeps')

# def func(*a):
#     print(*a, file=sys.stderr)
# func('Hello world')

# age = 17
# if age < 18:
#     # exits the program
#     sys.exit("Age less than 18")
# else:
#     print("Age is not less than 18")
# print('bye')

print(sys.modules)

a = 5
print(sys.getrefcount(a)) # 4294967295

print(sys.version) # python version
print(sys.argv) # path along with file_name

# random module

import random
print(random.random())
random.seed(7)
print(random.random())
# print("The mapped random number with 5 is : ", end="")

print(random.uniform(5, 10))

from datetime import datetime, timedelta

print('today: ',datetime.today())
date_str = '20/1/2025'
print(datetime.strptime(date_str, '%d/%m/%Y') + timedelta(days=365, hours=8, minutes=45))

import calendar
print(calendar.calendar(2025))

# print(calendar.weekday(2025,1,1))
ff = calendar.setfirstweekday(3)
print(ff)




