import socket

# Server configuration
HOST = '127.0.0.1'  # Localhost
PORT = 12345        # Port to connect to

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((HOST, PORT))

# Send username to server
username = input("Enter username: ")
client_socket.sendall(username.encode())

# Send password to server
password = input("Enter password: ")
client_socket.sendall(password.encode())

# Receive response from server
response = client_socket.recv(1024)
print("Server response:", response.decode())

# Close the connection
client_socket.close()
