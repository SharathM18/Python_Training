'''
Write a generator function that produces the Fibonacci sequence indefinitely.
Use yield to return the next number in the sequence.
'''

def fibonacci():
    num1 = 0
    num2 = 1
    while True:
        yield num1
        num3 = num1 + num2
        num1 = num2
        num2 = num3

total_fibonacci = int(input('total fibonacci: '))
fib_gen = fibonacci()

for _ in range(total_fibonacci):
    print(next(fib_gen)) # call yield not function itself
