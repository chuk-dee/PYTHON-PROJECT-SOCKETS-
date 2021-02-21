from socket import *

host = '192.168.43.171' #the ip of the LAN you have to getting by(typing ipconfig in the command prompt )
port = 8000
s = socket(AF_INET,SOCK_STREAM)
s.connect((host,port))  #connects the client to the server using the port and host
question = input("do you want to chat: ")
if question == "yes":
    name = input("what's your name: ")
    s.send(bytes(name,'utf-8'))
    while True:
        message = input("chuk-dee says: ") #this is the typed message sent to the server
        s.send(bytes(message,'utf-8')) #THIS SENDS THE MESSAGE TO THE SERVER in bytes
        print("awaiting reply")
        reply = s.recv(1024).decode() # THIS RECIEVES THE REPLY FROM THE SERVER in bytes(1024 is the max data it recieves)
        print(f"recieved from server:{repr(reply)} ") # THIS PRINTS THE recieved message from the server
        if reply == "quit":
            print("closed successfully")
            break
        
    s.close()