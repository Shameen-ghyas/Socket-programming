import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# Global variables
server_socket = None
client_socket = None
addr = None

#Function to handle incoming client messages
def receive_messages():
    global client_socket
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            chat_area.config(state='normal')
            chat_area.insert(tk.END, f"Client: {msg}\n")
            chat_area.config(state='disabled')
        except:
            break

# Function to send messages
def send_message():
    global client_socket
    msg = message_entry.get()
    if not msg.strip():
        return
    try:
        client_socket.send(msg.encode())
        chat_area.config(state='normal')
        chat_area.insert(tk.END, f"You: {msg}\n")
        chat_area.config(state='disabled')
        message_entry.delete(0, tk.END)
        if msg.lower() == 'exit':
            client_socket.close()
            server_socket.close()
            window.destroy()
    except:
        messagebox.showerror("Error", "No client connected yet!")

# Function to start the server
def start_server():
    global server_socket, client_socket, addr
    try:
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.bind(('localhost', 12345))
        server_socket.listen(1)
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "Server started on localhost:12345\nWaiting for client...\n")
        chat_area.config(state='disabled')

        # Run accept in a separate thread so GUI stays responsive
        threading.Thread(target=accept_connection, daemon=True).start()

    except Exception as e:
        messagebox.showerror("Error", f"Server failed to start:\n{e}")

#  Function that accepts a client connection 
def accept_connection():
    global client_socket, addr
    client_socket, addr = server_socket.accept()
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"Client connected from {addr}\n")
    chat_area.config(state='disabled')

    # Start thread for receiving messages
    threading.Thread(target=receive_messages, daemon=True).start()

#  GUI Setup 
window = tk.Tk()
window.title("Chat Server")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.pack(padx=10, pady=10)

message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(window, text="Send", command=send_message, width=10)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

start_button = tk.Button(window, text="Start Server", command=start_server, width=12)
start_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

window.mainloop()
