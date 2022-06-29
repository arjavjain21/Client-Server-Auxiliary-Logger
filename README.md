# Client-Server-Auxiliary-Logger
A simple python code using multiple sockets between client and server to connect to each other and keep a track of the data exchanged/communication in an auxiliary connected to both client and server.

Run the aux.py file to create the initial sockets to which the server and client can connect. 
The aux.py listens to the messages and communication done by the client and the server and prints them simultaneously.

Run the server.py file which initiates the server for the client to connect while at the same time connects with the open socket address provided to it by the auxiliary and sends the information (object) to the auxiliary.

Run the client.py which simply connects to the server and auxiliary and sends its message/object to both of them.

Finally, the auxiliary contains all the data exchanged between server and client and their socket addresses as well.


The purpose of this code is to keep a track of the communication between 2 bodies on a server and to make sure all of the communication is logged/stored in a separate helper client on the server. 
The situation is a simulation of blockchains when the transactions need to be stored, regardless of their success or failure during execution.
