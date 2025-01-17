# nested classes and how we can call
# how to declare main function in python
# how to create a module and access the module efficiently

import demo_module
from demo_module import increment

from demo_module import Demo
salary = Demo(40000, 10)
print(salary.add())

import os
current_dir = os.getcwd()
print(current_dir)

class person:

    def __init__(self, a):
        self.a = 10

    def __b(self):
        print('b')

    __b(6)

# print(person.a)
p = person(7)
# print(p.a)
# print(person().a)
# print(person.a)

