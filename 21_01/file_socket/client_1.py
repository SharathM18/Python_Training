import socket
import threading
from tkinter import *
import tkinter as tk
from tkinter import messagebox

def receive_messages():
    """Handles receiving messages from the server."""
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
    """Sends a message to the server."""
    message = message_entry.get()
    if message.strip():
        try:
            client_socket.send(message.encode('utf-8'))
            chat_window.config(state=NORMAL)
            chat_window.insert(END, f"You: {message}\n")
            chat_window.config(state=DISABLED)
            chat_window.see(END)
            message_entry.delete(0, END)
        except:
            messagebox.showerror("Error", "Failed to send message.")
    else:
        messagebox.showwarning("Warning", "Message cannot be empty!")

def on_closing():
    """Closes the client socket and exits the program."""
    try:
        client_socket.close()
    except:
        pass
    root.destroy()

def close_connection():
    """Closes the connection when the Close button is pressed."""
    on_closing()

# GUI setup
root = tk.Tk()
root.title("Chat Client")
root.geometry("400x500")
root.resizable(False, False)

# Chat display window
chat_window = Text(root, height=20, width=50, state=DISABLED, wrap=WORD)
chat_window.pack(pady=10)

# Message input field
message_entry = Entry(root, width=40)
message_entry.pack(pady=10)

# Send button
send_button = Button(root, text="Send", command=send_message)
send_button.place(x=50 * 14.5, y=400)

# Close button
close_button = Button(root, text="Close", command=close_connection)
close_button.place(x=50 * 12, y=400)

# Socket setup
try:
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect(('192.168.0.171', 9000))
    threading.Thread(target=receive_messages, daemon=True).start()
except Exception as e:
    messagebox.showerror("Connection Error", f"Unable to connect to server:\n{e}")
    root.destroy()

# Handle window close event
root.protocol("WM_DELETE_WINDOW", on_closing)

root.mainloop()