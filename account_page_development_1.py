# Imports
from pathlib import Path
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
from tkinter import messagebox
import sqlite3

# Set paths for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("account_page")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Function to update the canvas with user data
def update_canvas_with_data(canvas, text_ids, data):
    for text_id, text in zip(text_ids, data):
        canvas.itemconfig(text_id, text=text)


# Function to ask the user if they want to log out of their account which will direct users to login page if
# user wants to log out
def logout_option():
    response = messagebox.askquestion("Choose an option", "Would you like to logout? ")
    if response == 'yes':
        open_login()

    elif response == 'no':
        open_account_page()


# Functions that open different pages dependent on user choice,
# by destroying the current window and opening the relevant window by starting a new subprocess
# Function that opens the landing window
def open_landing():
    window.destroy()
    subprocess.Popen(['python', 'landing_page.py'])


# Functions that opens the vegetarian window
def open_vegetarian_page_1():
    window.destroy()
    subprocess.Popen(['python', 'vegetarian_mainpage.py'])


# Function that opens the gluten-free window
def open_gluten_free_page_1():
    window.destroy()
    subprocess.Popen(['python', 'glutenfree_mainpage.py'])


# Function that opens the vegan window
def open_vegan_page_1():
    window.destroy()
    subprocess.Popen(['python', 'vegan_mainpage.py'])


# Function that opens the keto window
def open_keto_page_1():
    window.destroy()
    subprocess.Popen(['python', 'keto_mainpage.py'])


# Function that opens the healthy window
def open_healthy_page_1():
    window.destroy()
    subprocess.Popen(['python', 'healthy_mainpage.py'])


# Function that opens the accounts window
def open_account_page():
    window.destroy()
    subprocess.Popen(['python', 'account_page.py'])


def open_login():
    window.destroy()
    subprocess.Popen(['python', 'login.py'])


# Functions to get user information from the database
# Function that extracts the name of the user from the database
def get_user_names():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT name FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchall()
        return [item[0] for item in data]
    finally:
        conn.close()


# Function that extracts the lastname of the user from the database
def get_user_lastnames():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT lastname FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchall()
        return [item[0] for item in data]
    finally:
        conn.close()


# Function that extracts the email of the user from the database
def get_user_emails():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT email FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchall()
        return [item[0] for item in data]
    finally:
        conn.close()


# Function that extracts the username of the user from the database
def get_user_usernames():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT username FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchall()
        return [item[0] for item in data]
    finally:
        conn.close()


offset = 1

# Function for main program


def main():
    global window
    # Create and configure main window
    window = Tk()
    window.title("DINE-EZ")
    window.geometry("1450x900")
    window.configure(bg="#FFFFFF")

    # Canvas to hold the user-interface elements for the window
    canvas = Canvas(
        window,
        bg="#FFFFFF",
        height=900,
        width=1450,
        bd=0,
        highlightthickness=0,
        relief="ridge"
    )

    canvas.place(x=0, y=0)

    # Placement of blank images for graphical interface on UI
    image_blank_2 = PhotoImage(file=relative_to_assets("blank2.png"))
    canvas.create_image(734.0, 545.0, image=image_blank_2)

    image_blank_3 = PhotoImage(file=relative_to_assets("blank3.png"))
    canvas.create_image(740.0, 445.0, image=image_blank_3)

    image_blank_4 = PhotoImage(file=relative_to_assets("blank4.png"))
    canvas.create_image(740.0, 522.0, image=image_blank_4)

    image_blank_5 = PhotoImage(file=relative_to_assets("blank5.png"))
    canvas.create_image(740.0, 599.0, image=image_blank_5)

    image_blank_6 = PhotoImage(file=relative_to_assets("blank6.png"))
    canvas.create_image(740.0, 676.0, image=image_blank_6)

    # Text labels on the canvas for user-interface navigation
    canvas.create_text(650, 340.0, anchor="nw", text="○ MY ACCOUNT",
                       fill="#000000", font=("Inter Light", 25))
    canvas.create_text(582.0, 630.0, anchor="nw", text="USERNAME:",
                       fill="#000000", font=("Inter ExtraLightItalic", 15))

    canvas.create_text(582.0, 557.0, anchor="nw", text="EMAIL:",
                       fill="#000000", font=("Inter ExtraLightItalic", 15))

    canvas.create_text(582.0, 402.0, anchor="nw", text="FIRST NAME:",
                       fill="#000000", font=("Inter ExtraLightItalic", 15))

    canvas.create_text(582.0, 481.0, anchor="nw", text="LASTNAME:",
                       fill="#000000", font=("Inter ExtraLightItalic", 15))

    # Text placeholders that will be replaced with user information from the database
    name = canvas.create_text(586.0, 438.0, anchor="nw", text="*FIRST NAME*",
                              fill="#000000", font=("Inter ExtraLightItalic", 11))
    names = [name]
    # Retrieve and update user-name from the database
    user_names = get_user_names()
    update_canvas_with_data(canvas, names, user_names)

    # These placeholders will be updated with the real restaurant names from the database
    lastname = canvas.create_text(586.0, 515.0, anchor="nw", text="*LASTNAME*",
                                  fill="#000000", font=("Inter ExtraLightItalic", 11))

    lastnames = [lastname]
    # Retrieve and update user last name from the database
    user_lastnames = get_user_lastnames()
    update_canvas_with_data(canvas, lastnames, user_lastnames)

    # These placeholders will be updated with the real restaurant names from the database
    email = canvas.create_text(586.0, 589.0, anchor="nw", text="*EMAIL*",
                               fill="#000000", font=("Inter ExtraLightItalic", 11))
    emails = [email]
    # Retrieve and update user emails from the database
    user_emails = get_user_emails()
    update_canvas_with_data(canvas, emails, user_emails)

    # These placeholders will be updated with the real restaurant names from the database
    username = canvas.create_text(586.0, 667.0, anchor="nw", text="*USERNAME*", fill="#000000",
                                  font=("Inter ExtraLightItalic", 11))
    usernames = [username]
    # Retrieve and update user usernames from the database
    user_usernames = get_user_usernames()
    update_canvas_with_data(canvas, usernames, user_usernames)

    # Disable window resizing on user interface
    window.resizable(False, False)

    # Start the Tkinter event loop
    window.mainloop()


# Ensures the main function is called when the script is executed directly
if __name__ == "__main__":
    main()
