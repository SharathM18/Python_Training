def func():
    yield 1,2
    yield 3
    yield 4
    print("after return the value it will execute print statement and in return keyword we can't done ")

print(next(func()))
print(next(func()))
print(next(func()))

for i in func():
    print(f'using for loop {i}')


def func_return():
    return 'return 1' # here it exists the function
    return 'return 2'
print(func_return())
'''
lst = [1,2,3,4,5]
obj = iter(lst)
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
print(next(obj))
'''

# yield keyword pause the operation and returns a value.
# and accept the value from send() and it continue with where it left

def numberGenerator(n):
    number = yield # None and 5,
    # print(number)
    while number < n:
        number = yield number
        print(f"while {number}")
        number += 1

g = numberGenerator(10)
print(g.__next__())# None
print(g.send(5))
print(g.send(6))
print(g.send(7))
print(g.send(8))
# print(g.send(9))

