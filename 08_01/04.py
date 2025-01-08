# matrix ROWSxCOLUMNS
'''
[[column,column, column], [column,column, column]]
<--       Row_1      -->   <--       Row_2      -->
'''

rows  = int(input("Enter the no. of rows: "))
column = int(input("Enter the no. of column: "))

matrix = []
for _ in range(rows):
    for _ in range(1):
        data = input("enter the data for row: ").split(' ')
        matrix.append(data)
print(matrix)

for i in range(len(matrix)):
    for j in range(len(matrix[0])):
        print(matrix[i][j], end=" ")
    print()

