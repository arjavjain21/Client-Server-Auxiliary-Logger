import socket
import pickle


class customer:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)

saux = socket.socket()
sser = socket.socket()

aport = 1234 # bw client and aux
sport = 9213 # bw client and server

saux.connect(('127.0.0.1',aport))
sser.connect(('127.0.0.1',sport))

msg=sser.recv(4029)

object=pickle.loads(msg)
print(object.name)
object.name='Arjav'
msg=pickle.dumps(object)

saux.send(msg)
sser.send(msg)

saux.close()
sser.close()