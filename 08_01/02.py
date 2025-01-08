'''
Convert this to dict. Use only dict comprehension. Note both key and value should be of int type.
string = "11 - 13, 12 - 14, 13 - 15"
'''

string = "11 - 13, 12 - 14, 13 - 15"
my_dict = {int(key.strip()): int(val.strip()) for key, val in (item.split('-') for item in string.split(','))}
print(my_dict)
