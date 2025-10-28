import socket

# Create a UDP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to localhost and port 12345
server_socket.bind(('localhost', 12345))
print("UDP Server started on localhost:12345 and waiting for messages...")

while True:
    # Receive message and client address
    data, client_address = server_socket.recvfrom(1024)
    message = data.decode()
    print(f"Received from {client_address}: {message}")

    # Echo the message back to the client
    server_socket.sendto(data, client_address)
    print(f"Echoed back to {client_address}\n")

    # If message is 'exit', close server
    if message.lower() == 'exit':
        print("Server shutting down...")
        break

server_socket.close()
