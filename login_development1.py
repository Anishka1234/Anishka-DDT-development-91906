# Imports
import sqlite3
from pathlib import Path
import subprocess
from tkinter import messagebox
from tkinter import Tk, Canvas, Entry, Button, PhotoImage
import os


# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("login")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def open_signup():
    subprocess.Popen(['python', 'signup.py'])


# Connecting to database
conn = sqlite3.connect("restaurants.db")
cursor = conn.cursor()


# Setting up log in page window
login_window = Tk()
login_window.title("DINE-EZ")
login_window.geometry("1450x900")
login_window.configure(bg="#FFFFFF")


def main():
    def validate_login():
        # Retrieve username and password user-input from entry fields
        username = username_entry2.get()
        password = password_entry2.get()

        if username != '' and password != '':
            # Select id and other user details where username and password match
            cursor.execute('SELECT id FROM users WHERE username = ? AND password = ?', (username, password))
            result = cursor.fetchone()
            if result:
                # Show success message
                messagebox.showinfo('Success', 'Logged in!')
            else:
                # Show error message if user login password or username are invalid
                messagebox.showerror('Error', 'Invalid username or password')

    # Graphical interface setup using Canvas and widgets, such as entry, labels, images
    canvas = Canvas(login_window, bg="#FCFCFC", height=900, width=1450, bd=0, highlightthickness=0)

    canvas.place(x=0, y=0)

    canvas.create_rectangle(168.0, 219.0, 569.0, 682.0, fill="#FFFFFF", outline="")

    # Submit button which validates user login
    button_image_submit = PhotoImage(
        file=relative_to_assets("submit.png"))
    button_submit = Button(image=button_image_submit, borderwidth=0, highlightthickness=0,
                           command=lambda: validate_login(), relief="flat")
    button_submit.place(x=467.0, y=508.0, width=92.0, height=51.0)

    # Username user entry
    username_entry2 = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
    username_entry2.place(x=240.0, y=364.0, width=256.0, height=48.0)

    # Password user entry
    password_entry2 = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0, show="*")
    password_entry2.place(x=240.0, y=450.0, width=256.0, height=48.0)

    # Text label for "LOGIN"
    canvas.create_text(344.0, 258.0, anchor="nw", text="LOGIN", fill="#000000", font=("Inter ExtraLightItalic", 20))
    # Text label for "USERNAME"
    canvas.create_text(235.0, 340.0, anchor="nw", text="USERNAME", fill="#000000", font=("Inter ExtraLightItalic", 15))
    # Text label for "PASSWORD"
    canvas.create_text(229.0, 422.0, anchor="nw", text="PASSWORD", fill="#000000", font=("Inter ExtraLightItalic", 15))

    login_window.mainloop()


# Disable window resizing on user interface
login_window.resizable(False, False)

if __name__ == "__main__":
    main()
