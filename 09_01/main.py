dict1 = {i: i**2 for i in range(1,11)}
print(dict1)

dict2 = {i: i **2 for i in range(2,11,2)}
print(dict2)

fruits = ['apple', 'banana','cherry']
dict3 = {i: len(i) for i in fruits}
print(dict3)

keys = ['name', 'age', 'gender']
dict4 = {i : None for i in keys}
print(dict4)

numbers = range(1, 11)
dict5 = {i: 'even' if i % 2==0 else 'odd' for i in numbers}
print(dict5)

keys = ['name', 'age', 'gender']
val = ['alice', 25, 'female']
# dict6 = {i :j for i,j in zip(keys, val)}
dict6 = {keys[i] :val[i] for i in range(len(keys))}
print(dict6)


dict7 = {chr(i):i for i in range(65, 91)}
print(dict7)

nested  = {'a':{'b':1, 'c':2},'d':{'e':3, 'f':4}}
dict8 ={f'{i}_{j}': nested[i][j] for i in nested.keys() for j in nested[i]}
print(dict8)

string = 'hello world'
# dict9 ={i: dict9[i]+1 if i in dict9 else 1 for i in string}
dict9 ={i: string.count(i) for i in string}
print(dict9)

# recursion function - 1000 iteration and depends on idle (RecursionError: maximum recursion depth exceeded)

import functools
lst = [1,2,3,4,5,6,7,8,9]
res = [functools.reduce(lambda a,b:a+b, lst, 1)] # initial default value is 0
# print(res)

def a():print('a')
def a(): print('b')
a()
