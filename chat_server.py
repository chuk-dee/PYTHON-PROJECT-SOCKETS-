from socket import *
import sqlite3
#from socket import socket,bind,listen,recv,send

host = '' #localhost or Lan ip
port = 8000
s = socket(AF_INET,SOCK_STREAM)
s.bind((host, port))
s.listen(3)         #how many connections it can recieve at a time
conn,addr = s.accept() #accept the connections
name = conn.recv(1024).decode()
print(f"connected by {addr}:{name}")  # print the address of the connected person
while True:
    data = conn.recv(1024).decode()   #recives the data in bytes using conn (1024 bytes is the max data it recieves)
    print(f"recieved from client:{data}") #prints the message that the user types
    reply = input("reply: ")    #replies the user
    conn.sendall(bytes(reply,'utf-8')) #sends the reply in bytes
    if reply == "quit":
        print("closed")
        break
        
    

conn.close()
connect = sqlite3.connect('saved_data.sqlite3')
action = connect.cursor()
action.execute('drop table if exists chats')
action.execute("create table chats(address float,name varchar(200),data varchar(200))")
action.execute("insert into chats(address,name,data) values(?,?,?)", (addr,name,data))
action.execute("select * where name = 'emma'")
c = action.fetchone()
print(c)
action.commit()



