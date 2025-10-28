import socket

# Create a TCP socket (IPv4, TCP)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Define host and port
host = '0.0.0.0'  
port = 9999      

# Bind the socket to the address
server_socket.bind((host, port))

# Start listening for a connection
server_socket.listen(1)
print(f"Server started on {host}:{port}, waiting for connection...")

# Accept a client connection
conn, addr = server_socket.accept()
print(f"Connected by {addr}")

while True:
    # Receive message from client
    data = conn.recv(1024).decode()
    if not data:
        print("Client disconnected.")
        break
    print(f"Client: {data}")

    # Get server message to send
    msg = input("You: ")
    conn.send(msg.encode())

conn.close()
