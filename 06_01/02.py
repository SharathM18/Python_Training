import math

def aoc(r):
    area = math.pi * (r**2)
    print(area)


status = True
while status:
    ip = int(input('Enter the area: '))
    if ip <= 0:
        print('enter a number above 0')
    else:
        aoc(ip)
        status = False



