'''
inputs:
l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]
output
lo=[6, 8, 1, 4, 8, 9, 2]
l0=l1+l2 with carry
'''
import time
print(time.time())

l1=[4,5,6,7]
l2=[2,3,5,6,7,9,2]

if len(l1) != len(l2):
    for i in range(len(l2) - len(l1)):
        l1.append(0)
res = []
carry = 0
for idx in range(len(l1)):
    addtion = l1[idx] + l2[idx] + carry
    carry = 0
    if addtion >= 10:
        bit = str(addtion)
        carry = int(bit[0])
        res.append(int(bit[1]))
    else:
        res.append(addtion)
print(time.time())
print(res)