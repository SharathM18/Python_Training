class Person:
    class_name = 'this is ClassName'

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def instance_method(self):
        print(self.name)

    @classmethod
    def class_method(cls, age):
        cls.res = age + 10
        print(Person.class_name, age, cls.res)

    @classmethod
    def class2(cls):
        print(cls.res)

    @staticmethod
    def static_method(rand_num, num):
        res = num * num
        print(Person.class_name, rand_num, res)

    # @staticmethod
    # def static2():
        # print(res)

    '''
    class and static method can't access the instance attributes and it can access class attributes.
    class method attribute can access another class method not instance method.
    static method attribute can access only in that method static method and it not share to other static method
    '''

person1 = Person('alex', 25000)
person1.instance_method()
person1.class_method(20)
person1.static_method(10, 15)
# person1.static2()
person1.class2()

class A:
    def __init__(self, num):
        super().__init__()
        print(num)
        print('a')
    def a1(self):
        print('a1')

class B:
    def __init__(self):
        print('b')

    def b1(self):
        print('b1')

class C(A, B):
    def __init__(self, num):
        super().__init__(num)
        print(num)
        print('c')
    def c1(self):
        print('c1')
        self.a1()
        self.b1()

bb = C(9)

'''
super().__init__() method useful when happens method overriding means same method name and parameters
it is useless for calling the other method like other than the method overriding

in inheritance we can call other method like self.<method_name>
'''