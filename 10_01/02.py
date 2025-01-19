'''
Write a generator that calculates the running sum of numbers sent to it using send.
If None is sent, it should return the current total.
'''

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