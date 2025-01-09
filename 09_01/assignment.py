'''
Capitalize names starting with the letter 'A' from the list
['Alice', 'Bob', 'Anna', 'Tom'].
Output:['ALICE', 'ANNA']
'''
lst1 = ['Alice', 'Bob', 'Anna', 'Tom']
res_lst1 = list(map(lambda ele: ele.upper(), filter(lambda filter_ele: filter_ele[0] == 'A', lst1)))
print(res_lst1)

'''
Find the square root of all positive numbers in 
[-4, 9, 16, -1, 25].
Output:[3.0, 4.0, 5.0]
'''
import math
lst2 = [-4, 9, 16, -1, 25]
res_list2 = list(map(lambda ele: float(math.sqrt(ele)), filter(lambda fil_ele: fil_ele >= 0, lst2)))
print(res_list2)

'''
Filter words containing the letter 'e' and convert them to uppercase. 
Words: ['apple', 'orange', 'pear', 'banana'].
Output:['APPLE', 'ORANGE', 'PEAR']
'''

lst3 = ['apple', 'orange', 'pear', 'banana']
res_lst3 = list(map(lambda ele: ele.upper(), filter(lambda fil_ele: 'e' in fil_ele, lst3)))
print(res_lst3)

'''
From the list of tuples [(1, 5), (3, 6), (4, 4), (2, 9)], 
filter tuples where the second element is greater than the first and compute their product.
Output:[5, 18, 18]
'''
lst4 = [(1, 5), (3, 6), (4, 4), (2, 9)]
res_lst4 = list(map(lambda a: a[0] * a[1], filter(lambda b: b[0] < b[1], lst4)))
print(res_lst4)

'''
Remove duplicate numbers from [2, 3, 2, 4, 5, 4] and calculate their squares.
Output: [4, 9, 16, 25]
'''
lst5 = [2, 3, 2, 4, 5, 4]
res_lst5 = list(map(lambda ele: ele**2,set(lst5)))
print(res_lst5)

'''
Filter numbers divisible by 4 in the range 0-20 and divide them by 2.
Output:[0.0, 2.0, 4.0, 6.0, 8.0, 10.0]
'''

res_lst6 = list(map(lambda ele: ele/2, filter(lambda fil_ele: fil_ele % 4 == 0, range(0,21))))
print(res_lst6)

'''
For odd numbers in 0-9, calculate the sum of their squared digits.
Output:[1, 9, 25, 49, 81]
'''
res_lst7 = list(map(lambda ele: ele**2, filter(lambda fil_ele: fil_ele % 2 != 0, range(0,10))))
print(res_lst7)

'''
Find all numbers in the range 1-50 that are divisible by both 3 and 5.
Output: [15, 30, 45]
'''
res_lst8 = list(filter(lambda ele: ele % 3 == 0 and ele % 5 == 0, range(1,50)))
print(res_lst8)

'''
Filter out vowels from the list 
['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z'].
Output:['a', 'e', 'i', 'o', 'u']
'''
lst9 = ['a', 'b', 'c', 'e', 'i', 'o', 'u', 'z']
res_lst9 = list(filter(lambda ele: ele in 'aeiou', lst9))
print(res_lst9)

'''
Find the lengths of words longer than 4 characters in the list 
['apple', 'is', 'tasty', 'cherry', 'banana'].
words = ['apple', 'is', 'tasty', 'cherry', 'banana']
output: [5, 5, 6]
'''
words = ['apple', 'is', 'tasty', 'cherry', 'banana']
res_lst10 = list(map(lambda ele: len(ele), filter(lambda fil_ele: len(fil_ele)> 4, words)))
print(res_lst10)

'''
Filter palindromes from the list ['madam', 'hello', 'radar', 'world', 'level'].
Output:['madam', 'radar', 'level']
'''
lst11 = ['madam', 'hello', 'radar', 'world', 'level']
res_lst11 = list(filter(lambda ele: ele == ele[::-1], lst11))
print(res_lst11)

'''
Calculate the base-10 logarithm of numbers greater than 0 in 
[1, 10, 100, 0, 1000].
Output:[0.0, 1.0, 2.0, 3.0]
'''
lst12 = [1, 10, 100, 0, 1000]
res_lst12 = list(map(lambda ele: math.log10(ele), filter(lambda fil_ele: fil_ele > 0, lst12)))
print(res_lst12)

'''
Filter prime numbers in the range 0-49.
Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47]
'''

# res_lst13 = list(filter(lambda ele: ele % 2 != 0, range(2,49)))
# print(res_lst13)

# for i in range(2,49):
#     for j in range(2,i):
#         if i%j==0:
#             break
#     else:
#         print(i)