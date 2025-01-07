print('hi \r\n bro')
print('h\vi \f bro in\x20to hel\blo') # \x20: space

# exit() used anywhere in the program and Terminates the entire Python program immediately
# break used in for and while, Terminates the innermost loop
n = 1
while n <= 10:
    print(n)
    if n == 5:
        # exit()
        break
    n += 1


outter = 1
while outter <= 5:
    print(outter)
    inner = 0
    while True:
        inner += 1
        print(f'{outter}.{inner}')
        if inner == 9:
            break
    outter += 1

ip = eval(input('Enter anythings: ')) # used for maths operations
print(type(ip))

a = [1,2,3,4]
res = list(map(lambda num: num + 5, a))
print(res)

def reverse_string(a):
    return list(reversed(a))

ip = input("enter: ").split(' ')
print(reverse_string(ip))

mydict = []
print(dir(mydict))

'''
List [] - .append(value), .extend([] or value), pop() or pop(index), remove(value), del, .copy(), insert(index, value), .sort() or .sort(reversed = True), .count(value), .index(value), .clear(), .reverse()
Tuple () - +, del, .count(value), .index(value)
Dict {} - .key(), .values(), .items(), .get(key), [key] = value, .update({}), .clear(), .popitem(), .pop(key), del, .copy()
Set - .add(value), .update({} or value), .copy(), .pop(), .remove(value), .clear()
'''