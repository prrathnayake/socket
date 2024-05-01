import socket
import hashlib
import hmac

# Server configuration
HOST = '127.0.0.1' 
PORT = 12345       
SECRET = b'my_secret'

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client_socket.connect((HOST, PORT))

username = input("Enter username: ")
client_socket.sendall(username.encode())

password = input("Enter password: ")
password_hash = hashlib.sha256(password.encode()).hexdigest()
client_socket.sendall(password_hash.encode())

response = client_socket.recv(1024)
print("Server response:", response.decode())

client_socket.close()
