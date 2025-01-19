mydic = {'a': None} #unorder collection and order wrt key
# float, int, small letter, big letter

lst = [1,2,3,0.5,] # it should be in one type in order to work sort()
lst.sort()
print(len(lst))

# sorted dictionary
d = {'ravi': 10, 'rajnish': 9, 'sanjeev': 15}
myKeys = list(d.keys())
myKeys.sort()
sd = {i: d[i] for i in myKeys}
print(sd)

# default datatype is tuple

# join() accept one argus

def func(lst, string):
    num_lst = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    str_list = [string[i] for i in range(len(string)) if i % 2 != 0][::-1]
    final_lst = [i for tuple_pair in zip(num_lst, str_list) for i in tuple_pair]
    return final_lst
a = [1,2,3,4,5,6,7,8,9,10]
b = 'abcdefghi'
print(func(a,b))

transposed = []
matrix = [[1,2,3,4],[4,5,6,8]]
for i in range(len(matrix[0])):
    trans_row = []
    for j in matrix:
        # print(j)
        trans_row.append(j[i])
    transposed.append(trans_row)
print(transposed)

lst = [[matrix[0][i], j] for i in range(len(matrix[0])) for j in [matrix[1][i]]]
print(lst)

ele1, ele2 = matrix
transposed = [[i, j] for i, j in zip(ele1, ele2)]

lst = [(1,2),(3,4)]
print(dict(lst)) # {1: 2, 3: 4}

# union |
# intersection &
# difference -
# symmetric difference ^

