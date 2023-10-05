import socket
def server_program():
    host=socket.gethostname()
    port=8000
    server_socket=socket.socket()
    server_socket.bind((host,port))
    server_socket.listen(2)
    connection,address=server_socket.accept()
    while True:
        data=connection.recv(1024).decode()
        if not data:
            break
        print(data)
        message=input('enter your message : ')
        connection.send(message.encode())
    connection.close()

if __name__ =="__main__":
    server_program()
