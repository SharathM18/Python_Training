import socket
s=socket.socket()
print('socket created')
#bind takes 1 agr so give both local host and port no. as 1(inside 1 bracket)
s.bind(('192.168.0.216',9000))
#instead of localhost collect the ipaddress
#and try with 2 different machines
#no of clients=3 here
s.listen(3)
print('Waiting for connections...')
while True:
    c, addr=s.accept()
    name=c.recv(1024).decode()
    print('connected with ',addr,name)
    #always send the msg in byte format
    c.send(bytes('welcome to our server','utf-8'))
    c.close()