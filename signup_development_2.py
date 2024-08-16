# Imports
import sqlite3
from pathlib import Path
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import re

# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("signup")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function which validate password requirements,
# this includes password length and at least on numerical value in user password
def validate_password(password):
    # Password is checked to validate that the password is more than 6 characters long
    if len(password) <= 6:
        return False, 'Password must be more than 6 characters long'
    # Password is checked to validate the user password contains at least one number
    return True, ''


# Function which validate email format which user has entered into the entry box
def validate_email(email):
    # Validates whether user email entered contains '@' and '.'
    if '@' not in email or '.' not in email:
        return False, 'Invalid email'
    return True, ''


# Function which handle the signup process for users
def main():
    # Get input from entry widgets
    name = entry_name.get()
    lastname = entry_lastname.get()
    email = entry_email.get()
    username = entry_username.get()
    password = entry_password.get()
    re_password = entry_repassword.get()

    # Validates if all entry fields are not empty
    if name != '' and lastname != '' and email != '' and username != '' and password != '' and re_password != '':
        # Check if the username already exists in the database
        cursor.execute('SELECT username FROM users WHERE username=?', (username,))
        if cursor.fetchone() is not None:
            messagebox.showerror('Error', 'Username already exists')
        elif password != re_password:
            messagebox.showerror('Error', 'Your passwords do not match')
        else:
            # Validation of email and password
            is_valid_email, message_email = validate_email(email)
            is_valid_password, message_password = validate_password(password)
            if not is_valid_email:
                messagebox.showerror('Error', message_email)
            elif not is_valid_password:
                messagebox.showerror('Error', message_password)
            else:
                # New user is entered into the database
                cursor.execute('INSERT INTO users (name, username, password, email, lastname) VALUES (?, ?, ?, ?, ?)',
                               (name, username, password, email, lastname))
                conn.commit()
                messagebox.showinfo('Success', 'You have successfully signed up. Please login.')
                window.destroy()  # Signup window is closed
    else:
        messagebox.showerror('Error', 'Please fill out all fields')


# Dimensions of the window set
window_width = 636
window_height = 679

# Initialize signup_window
window = Tk()
window.title("DINE-EZ")
window.geometry("636x679")
window.configure(bg="#FFFFFF")


# Canvas to hold the user-interface elements for the window
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=679,
    width=636,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)

# Set up the SQLite connection with database
conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()

# Table is created the table it doesn't already exist
cursor.execute('''
CREATE TABLE IF NOT EXISTS users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    username TEXT NOT NULL,
    password TEXT NOT NULL,
    email TEXT NOT NULL,
    lastname TEXT NOT NULL
)
''')


# Text labels on UI for user navigation
# Text label for "USERNAME:"
canvas.create_text(165.0, 366.0, anchor="nw", text="USERNAME:", fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "EMAIL:"
canvas.create_text(165.0, 293.0, anchor="nw", text="EMAIL:", fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "PASSWORD:"
canvas.create_text(165.0, 439.0, anchor="nw", text="PASSWORD ( Must contain at-least 6 \n characters & 1 numeric ) :",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "RE-TYPE PASSWORD:"
canvas.create_text(165.0, 536.0, anchor="nw", text="RE-TYPE PASSWORD:",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))
# Text label for "FIRST NAME:"
canvas.create_text(165.0, 138.0, anchor="nw", text="FIRST NAME:", fill="#000000",
                   font=("Inter ExtraLightItalic", 15))
# Text label for "LAST NAME:"
canvas.create_text(165.0, 217.0, anchor="nw", text="LAST NAME:",
                   fill="#000000", font=("Inter ExtraLightItalic", 15))

# First name user entry
entry_name = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_name.place(x=180.0, y=159.0, width=256.0, height=48.0)

# Lastname user entry
entry_lastname = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_lastname.place(x=180.0, y=240.0, width=256.0, height=48.0)

# Email user entry
entry_email = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_email.place(x=180.0, y=311.0, width=256.0, height=48.0)

# Username user entry
entry_username = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
entry_username.place(x=180.0, y=384.0, width=256.0, height=48.0)

# Password user entry
entry_password = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0, show="*")
entry_password.place(x=180.0, y=476.0, width=256.0, height=48.0)

# Re-entry password user entry
entry_repassword = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0, show="*")
entry_repassword.place(x=180.0, y=557.0, width=256.0, height=48.0)


window.resizable(False, False)
# Start the Tkinter main loop
window.mainloop()
