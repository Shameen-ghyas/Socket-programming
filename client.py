import socket
import threading
import tkinter as tk
from tkinter import scrolledtext, messagebox

# --- Client logic ---

def connect_to_server():
    try:
        client_socket.connect(('localhost', 12345))
        chat_area.config(state='normal')
        chat_area.insert(tk.END, "Connected to the server!\n")
        chat_area.config(state='disabled')
        connect_button.config(state='disabled')
        threading.Thread(target=receive_messages, daemon=True).start()
    except Exception as e:
        messagebox.showerror("Connection Error", f"Could not connect to server.\n{e}")

def receive_messages():
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if not msg:
                break
            chat_area.config(state='normal')
            chat_area.insert(tk.END, f"Server: {msg}\n")
            chat_area.config(state='disabled')
        except:
            break

def send_message():
    msg = message_entry.get()
    if msg.strip() == "":
        return
    client_socket.send(msg.encode())
    chat_area.config(state='normal')
    chat_area.insert(tk.END, f"You: {msg}\n")
    chat_area.config(state='disabled')
    message_entry.delete(0, tk.END)
    if msg.lower() == 'exit':
        client_socket.close()
        window.destroy()


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

window = tk.Tk()
window.title("Chat Client")

chat_area = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=20, state='disabled')
chat_area.pack(padx=10, pady=10)

message_entry = tk.Entry(window, width=40)
message_entry.pack(side=tk.LEFT, padx=(10, 0), pady=(0, 10))

send_button = tk.Button(window, text="Send", command=send_message, width=10)
send_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

connect_button = tk.Button(window, text="Connect", command=connect_to_server)
connect_button.pack(side=tk.LEFT, padx=10, pady=(0, 10))

window.mainloop()
