name = input('name: ')
ip = input('Enter the name of products stored in the cotton box: ').split(',')
res = []
for i in ip:
    if 'teddy' in i:
        res.append(i)
print(f'Dear {name} \nTotal {len(res)} teddies are there. And, here they are: \n{res}')