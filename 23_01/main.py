import tkinter as tk
from tkinter import messagebox

# Simulated database as a dictionary
user_database = {
    "John Doe": "john.doe@example.com",
    "Jane Smith": "jane.smith@example.com",
    "Alice Johnson": "alice.johnson@example.com",
    'alex': 'alex@alex.com'
}

# Function to handle login
def authenticate():
    name = entry_name.get().strip()
    email = entry_email.get().strip()

    if not name or not email:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    # Check if name and email match the "database"
    if name in user_database and user_database[name] == email:
        show_welcome_message(name)  # Replace login with welcome message
    else:
        messagebox.showerror("Login Failed", "Invalid name or email!")

# Function to show welcome message in the same window
def show_welcome_message(name):
    # Clear the window
    for widget in root.winfo_children():
        widget.destroy()

    # Display the welcome message
    tk.Label(
        root,
        text=f"Welcome, {name}!",
        font=("Arial", 20, "bold"),
        bg="lightblue",
        fg="darkblue"
    ).pack(expand=True, fill="both")

    # Add an exit button
    tk.Button(
        root,
        text="Exit",
        font=("Arial", 12),
        bg="red",
        fg="white",
        command=root.destroy
    ).pack(pady=20)

# Main application window
root = tk.Tk()
root.title("Login System")
root.geometry("400x300")
root.configure(bg="white")

# Title label
tk.Label(root, text="Login System", font=("Arial", 16, "bold"), bg="white").pack(pady=10)

# Name label and entry
tk.Label(root, text="Name:", font=("Arial", 12), bg="white").pack(pady=5)
entry_name = tk.Entry(root, font=("Arial", 12), width=30)
entry_name.pack(pady=5)

# Email label and entry
tk.Label(root, text="Email:", font=("Arial", 12), bg="white").pack(pady=5)
entry_email = tk.Entry(root, font=("Arial", 12), width=30)
entry_email.pack(pady=5)

# Submit button
tk.Button(
    root,
    text="Submit",
    font=("Arial", 12),
    bg="blue",
    fg="white",
    command=authenticate
).pack(pady=20)

# Run the application
root.mainloop()