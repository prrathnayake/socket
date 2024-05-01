import socket
import hashlib
import hmac

# Server configuration
HOST = '127.0.0.1'  
PORT = 12345        
USERNAME = 'user'
PASSWORD_HASH = hashlib.sha256(b'password').hexdigest()

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind((HOST, PORT))

server_socket.listen(1)
print("Server is listening on port", PORT)

connection, address = server_socket.accept()
print("Connected by", address)

username = connection.recv(1024).decode()
print("Received username:", username)

password_hash = connection.recv(1024).decode()
print("Received password hash:", password_hash)

if username == USERNAME and password_hash == PASSWORD_HASH:
    connection.sendall(b'Success')
else:
    connection.sendall(b'Failure')

connection.close()
