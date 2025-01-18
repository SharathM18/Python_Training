database = {'s1':['red','Silk',4500],
            's2':['blood red','Silk',11500],
            's3':['pink','Silk',11200],
            's4':['rose red','Party wear',6999],
            's5':['lemon yellow','Silk',8500],
            's6':['brick red','Silk',8500],
            's7':['Green','Party wear',8999],
            's8':['brick red','cotton',1500],
            's9':['Candy red','Silk',8500],
            's10':['Ruby red','Silk',9999]
            }

res = list(filter(lambda a: 'red' in database[a][0] and database[a][1] == 'Silk' and database[a][2] <= 10000, database))
print(res)