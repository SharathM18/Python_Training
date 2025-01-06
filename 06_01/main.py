from dataclasses import replace

s = 'Hi Sharath'
a = 'Hi Sharath'

print(s)
# print(s[::-1])
# print(s[-190:-8])
# print(s[:-8])
# print(s[::-1])
# print(s[:-2:-1])

# print(s[3:] +' '+ s[:2])

# print(s is a)
# print('a' in s)

# print(s**2)

# print(ord('A'))
# print(ord('a'))

# print('int :%2d, float :%5.4f, oct :%5.4o' %(234, 56.546789, (25)))

# print('hi {1} "{0}"'.format('bro', 'whats up'))

# print('hi sharath \t \n whats up?')
# print(r'hi sharath \t \n whats up?') # r: raw string

# print('hi sharath \r whats up?') # carriage return
# print(r'hi sharath \t \r whats up?')

# c = s.center(10,'#') # not working
# print(c)

# print(s.find('a')) # -1
# print(s.index('a')) # value error
# print(s.rindex('a')) # reverse index
# print(s.rfind('a')) # reverse find

# Falsely value: [], (), {}, set(), 0, False

# print(~10)
# print(~~3)

string = 'shÀrÁth'
res = string.encode() # ignore, replace
print(res, type(res))

res_decode = res.decode()
print(res_decode, type(res_decode))









