import sqlite3
import bcrypt
import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.geometry("450x600")
root.configure(bg="#FCFCFC")

# Set up the SQLite connection
conn = sqlite3.connect("data.db")
cursor = conn.cursor()

# Create a sample table if it doesn't exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    username TEXT NOT NULL,
    password TEXT NOT NULL
)
''')

def signup():
    username = entry_username.get()
    password = entry_password.get()
    if username != '' and password != '':
        cursor.execute('SELECT username FROM users WHERE username=?', (username,))
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')
        else:
            encoded_password = password.encode('utf-8')
            hashed_password = bcrypt.hashpw(encoded_password, bcrypt.gensalt())
            cursor.execute('INSERT INTO users (username, password) VALUES (?, ?)', (username, hashed_password))
            conn.commit()
            messagebox.showinfo('Success', 'You have successfully signed up!')
    else:
        messagebox.showerror('Error', 'Please fill out all fields')

# Create and place the labels and entries
label_username = tk.Label(root, text="Username", bg="#FCFCFC")
label_username.grid(row=0, column=0, padx=10, pady=5)

entry_username = tk.Entry(root)
entry_username.grid(row=0, column=1, padx=10, pady=5)

label_password = tk.Label(root, text="Password", bg="#FCFCFC")
label_password.grid(row=1, column=0, padx=10, pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.grid(row=1, column=1, padx=10, pady=5)

# Create and place the submit button
button_submit = tk.Button(root, text="Submit", command=signup)
button_submit.grid(row=2, columnspan=2, pady=10)

# Run the main event loop
root.mainloop()

# Commit the transaction and close the connection when the program ends
conn.commit()
conn.close()