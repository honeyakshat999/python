import socket
import re
import sys

#creating a function

def func1(ip,user,password):
    sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  #here we use socket library
    print "trying" +_ip + ":" + user + ":" +password
    sock.connect('10.2.65.2',80)  #here we specify ip  and port


    data=sock.recv(1024)
    sock.send('user'+ user +'\r\n')

    data = sock.recv(1024)

    sock.send("password" + password + '\r\n')

    data = sock.recv(1024)

    sock.send("quit" * '\r\n')
    sock.close()

    return data
#ip="10.2.65.2"
user='user1'
password=['pass1','pass2','pass3']

for pas in password:
    print func1('10.2.65.2',user,password)