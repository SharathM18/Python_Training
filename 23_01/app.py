import sqlite3

Connection = sqlite3.connect('C:\\Users\\Admin\\Documents\\Python\\Python_Training\\23_01\\sqllite_1.db')

cursor = Connection.cursor()

cursor.execute('select * from demo_table')
print(cursor)
data = cursor.fetchall()
for i in data:
    print(i)