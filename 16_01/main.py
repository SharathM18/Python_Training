'''
abstract class: adding a extra layer of security to the class
- when we write ABC it should be abstract class
- when we write @abstractmethod then it should be called as abstract method
- and these method should be in every class, and you can add other method also
'''
from abc import abstractmethod, ABC

class P1(ABC):
    @abstractmethod
    def a(self): pass
    @abstractmethod
    def c(self):pass

class Parent_1(P1):
    def a(self):print('a')
    def c(self):print('a')

    def d(self): print('d')

class Parent_2(P1):
    def a(self):print('aa')
    def c(self):print('c')
    def d(self):print('d')

ppp = Parent_1()
ppp.d()

'''
access specifier are used to control the visibility and accessibility of class members (attributes and methods)
- They are meant to guide developers, not prevent access. and it does not provide any security.
- public, protected(_attributes/method), private(__attributes/method) 
same class, derived class, different/ new object
public: 1, 1, 1
protected: 1, 1, 0
private: 1, 0, 0
'''

class MyClass:
    def __init__(self):
        self.public_var = 10  # Public variable
        self._protected_var = 20  # Protected variable
        self.__privatevar = 30  # Private variable

    def public_method(self):
        print("Public method")

    def _protected_method(self):
        print("Protected method")

    def __private_method(self):
        print("Private method")

obj = MyClass()

print(obj.public_var)
print(obj._protected_var)
# print(obj.__private_var)  # Error, can't access private member directly
print(obj._MyClass__privatevar)

print(obj._protected_method())
print(obj._MyClass__private_method())



class bill:
    def __init__(self, m, n):
        self.m = m
        self.n = n

    def __add__(self, other):
        a = self.m + self.m
        b = self.n + self.n

        return self.__gt__(a, b)

    def __gt__(self, other):
        res = self.a > self.b
        return res

a1 = bill(5000, 15000)
a2 = bill(25000, 5000)

re = a1 > a2
if re:
    print('a1 is greater')
else:
    print('b1 is greater')

def add(a,b):
    print(a+b)

def add(a,b,c=0):
    print(a+b+c)

add(1,2)
add(1,2,3)

