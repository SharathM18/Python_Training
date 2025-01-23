import socket
import threading
from tkinter import *
import tkinter as tk

def receive_messages():
    while True:
        try:
            message = client_socket.recv(1024).decode('utf-8')
            if message:
                chat_window.config(state=NORMAL)
                chat_window.insert(END, f"Peer: {message}\n")
                chat_window.config(state=DISABLED)
                chat_window.see(END)
        except:
            print("An error occurred while receiving messages.")
            client_socket.close()
            break

def send_message():
    message = message_entry.get()
    if message:
        client_socket.send(message.encode('utf-8'))
        chat_window.config(state=NORMAL)
        chat_window.insert(END, f"You: {message}\n")
        chat_window.config(state=DISABLED)
        chat_window.see(END)
        message_entry.delete(0, END)

def on_closing():
    client_socket.close()
    root.destroy()

# GUI setup
root = tk.Tk()
root.title("Chat Client")
root.geometry("400x500")

chat_window = Text(root, height=20, width=50, state=DISABLED)
chat_window.pack(pady=10)

message_entry = Entry(root, width=40)
message_entry.pack(pady=10)

send_button = Button(root, text="Send", command=send_message)
send_button.place(x=50*14.5   , y=400)

def close_connection():
    try:
        client_socket.close()  # Close the socket connection
    except:
        pass  # Handle any potential errors (e.g., socket already closed)
    root.destroy()  # Close the tkinter window

okay = tk.Button(root, text="Close", command=close_connection)
okay.place(x=50*12, y=400)

# Socket setup
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('localhost', 9000))

# Start receiving messages in a separate thread
threading.Thread(target=receive_messages, daemon=True).start()

root.protocol("WM_DELETE_WINDOW", on_closing)
root.mainloop()