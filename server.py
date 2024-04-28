import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to listen on
USERNAME = 'user'
PASSWORD = 'password'

# Create a socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the address
server_socket.bind((HOST, PORT))

# Listen for incoming connections
server_socket.listen(1)
print("Server is listening on port", PORT)

# Accept incoming connection
connection, address = server_socket.accept()
print("Connected by", address)

# Receive username from client
username = connection.recv(1024).decode()
print("Received username:", username)

# Receive password from client
password = connection.recv(1024).decode()
print("Received password:", password)

# Authenticate
if username == USERNAME and password == PASSWORD:
    connection.sendall(b'Success')
else:
    connection.sendall(b'Failure')

# Close the connection
connection.close()
