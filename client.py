import socket
def client_program():
    host=socket.gethostname()
    port=8000
    client_socket=socket.socket()
    client_socket.connect((host,port))
    message=input('enter your message')
    while(message.lower().strip()!='bye'):
        client_socket.send(message.encode())
        data=client_socket.recv(1024).decode()
        print(data)
        message=input("enter your message:")
    client_socket.close()

if __name__ =="__main__":
                      client_program()
