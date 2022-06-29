import socket
import pickle


class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

c1 = customer("Arjav",20)

msg=pickle.dumps(c1)

sclient = socket.socket() # aux-client socket
sserver = socket.socket() # aux-server socket
print("Sockets created ")

host="127.0.0.1"
cport = 1234 # bw aux and client
sport = 5678 # bw aux and server

sclient.bind((host, cport))
sserver.bind((host, sport))

print("Client Socket binded to port: " + str(cport))
print("Server Socket binded to port: " + str(sport))

sserver.listen()
sclient.listen()

while True:

    sconn,saddr = sserver.accept()
    clconn,claddr = sclient.accept()

    print("Server: ",saddr)
    print("Client: ",claddr)

    smsg = sconn.recv(4096)
    if(smsg):
        sobject = pickle.loads(smsg)
        print("Server: " +sobject.name)

    clmsg = clconn.recv(4096)
    if(clmsg):
        clobject = pickle.loads(clmsg)
        print("Client: " +clobject.name)

    if(not smsg or not clmsg):
        print("Timeout")
        break
    
    sconn.close()
    clconn.close()
    break