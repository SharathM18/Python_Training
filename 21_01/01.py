# Inside folder find out how many files and folders, file_name, date_created, extension.

import os
import time
from os.path import isfile, isdir

contents = os.listdir()
directory = {}
files = {}
for i in contents:
    if isfile(i):
        files[i.split('.')[0]] = [i.split('.')[1], time.ctime(os.stat(i).st_ctime)]
    elif isdir(i):
        directory[i] = time.ctime(os.stat(i).st_ctime)

print(f'Total folder: {len(directory)}')
for i, j in directory.items():
    print(f'Folder name: {i}, Time created: {j}')

print(f'Total files: {len(files)}')
for i, j in files.items():
    print(f'Files name: {i}, Extension: {j[0]}, Created time: {j[1]}')