'''
Convert this to dict. Use only dict comprehension.
string = "A - 13, B - 14, C - 15"
'''

string = "A - 13, B - 14, C - 15"
my_dict = {i.strip(): j.strip() for i, j in (i.split('-') for i in string.split(','))}
print(my_dict)

my_dict_res = {}
for item in string.split(','):
    key, val = item.split('-')
    my_dict_res.update({key.strip(): val.strip()})
print(my_dict_res)


