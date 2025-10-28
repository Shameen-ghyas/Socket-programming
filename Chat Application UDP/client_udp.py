import socket

# Create a UDP socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server_ip = 'localhost'
server_port = 12345

print("Type messages to send to the server. Type 'exit' to quit.\n")

while True:
    message = input("You: ")
    client_socket.sendto(message.encode(), (server_ip, server_port))

    # Receive echoed message from server
    data, _ = client_socket.recvfrom(1024)
    print(f"Server echoed: {data.decode()}\n")

    if message.lower() == 'exit':
        print("Closing client...")
        break

client_socket.close()
