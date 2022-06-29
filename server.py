import socket
import pickle


class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

c1 = customer("Rohit",21)

msg=pickle.dumps(c1)


saux = socket.socket()
scli = socket.socket()
print("Sockets created ")

host="127.0.0.1"
aport = 5678 # bw aux and server
cport = 9213 # bw server and client

saux.connect((host,aport))

scli.bind((host,cport))

print("Server socket binded to port: " + str(cport))

scli.listen()

while True:

    clconn, claddr = scli.accept()
    print("Connected to ",claddr)

    saux.send(msg)
    clconn.send(msg)
    
    clmsg = clconn.recv(4096)
    if(not clmsg):
        print("Timeout")
        break

    else:
        clobject=pickle.loads(clmsg)
        print(clobject.name)

    clconn.close()
    break