# Imports
from pathlib import Path
from tkinter import Tk, Canvas, Entry, Button, PhotoImage, messagebox
import sqlite3
import os
import subprocess


# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("write_reviews")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Fetch user ID from environment variables
user_idnum = os.getenv('user_idnum')
if user_idnum is not None:
    user_id = int(user_idnum)
else:
    user_id = 1  # Set default user_id if environment variable is not set

offset = user_id - 1


# Function which fetches the username from the database based on offset
def get_usernames():
    global offset
    conn = sqlite3.connect('restaurants.db')
    cursor = conn.cursor()
    try:
        query = f'SELECT username FROM users LIMIT 1 offset {offset}'
        cursor.execute(query)
        data = cursor.fetchone()
        if data:
            return data[0]
        else:
            return None
    finally:
        conn.close()


# Function to open the review submission script
def open_reviews():
    subprocess.Popen(['python', 'andiamo_submit_reviews.py'])


# Function to validate if the review submission script exists and open it
def open_submit_reviews():
    print("Opening submit reviews...")
    script_path = 'andiamo_submit_reviews.py'
    if os.path.exists(script_path):
        print("Script found.")
        window.destroy()
        subprocess.Popen(['python', script_path])
    else:
        print("Script not found.")


# Function which handles review submission
def submit_review():
    review_text = user_review.get()
    username = get_usernames()

    if review_text != '' and username:
        review_with_quotes = f':  " {review_text} "'
        conn = sqlite3.connect('restaurants.db')
        cursor = conn.cursor()
        try:
            cursor.execute('''
                INSERT INTO andiamo_reviews (username, user_review) VALUES (?, ?)
            ''', (username, review_with_quotes))
            conn.commit()
        finally:
            conn.close()
            user_review.delete(0, 'end')  # Clear the entry after submission
            response = messagebox.askquestion("Choose an option", "REVIEW SUBMITTED! \n "
                                                                  "Would you like to submit another review?")
            if response == 'yes':
                open_reviews()

            elif response == 'no':
                window.destroy()
    else:
        messagebox.showerror('Error', 'Please write a review')


# Initialize main window
window = Tk()
window.title("DINE-EZ")
window.geometry("545x446")
window.configure(bg="#FFFFFF")

# Connect to the reviews database and create the reviews table for restaurant  if it doesn't exist
conn = sqlite3.connect('restaurants.db')
cursor = conn.cursor()
cursor.execute('''
    CREATE TABLE IF NOT EXISTS andiamo_reviews (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT NOT NULL,
        user_review TEXT NOT NULL
    )
''')
conn.commit()
conn.close()

# Tkinter canvas and widgets setup
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=446,
    width=545,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)
canvas.place(x=0, y=0)

# Load and place the entry background image
entry_image = PhotoImage(file=relative_to_assets("entry_background_image.png"))
entry_bg = canvas.create_image(273.0, 270.0, image=entry_image)

# Create and place the entry widget for review input
user_review = Entry(bd=0, bg="#F6F6F5", fg="#000716", highlightthickness=0)
user_review.place(x=111.0, y=241.0, width=324.0, height=56.0)

window.mainloop()
