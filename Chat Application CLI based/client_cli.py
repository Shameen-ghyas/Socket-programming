import socket

# Create a TCP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)


host = '127.0.0.1'  # Use '127.0.0.1' if testing on same device
port = 9999

# Connect to server
client_socket.connect((host, port))
print(f"Connected to server {host}:{port}")

while True:
    # Get message from user
    msg = input("You: ")
    client_socket.send(msg.encode())

    # Receive reply from server
    data = client_socket.recv(1024).decode()
    print(f"Server: {data}")

client_socket.close()
