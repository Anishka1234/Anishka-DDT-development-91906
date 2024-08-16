# Imports
from pathlib import Path
import webbrowser
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import os
from tkinter import Tk, Canvas, Button, PhotoImage
import subprocess
from tkinter import Menu

# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("main_page_frames")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Retrieval restaurant data from the database
def retrieve_restaurant_data():
    db_path = 'restaurants.db'
    if not os.path.exists(db_path):
        messagebox.showerror("Error", "Database file not found.")
        return []

    try:
        conn = sqlite3.connect(db_path)
        c = conn.cursor()
        c.execute("SELECT image_path, website FROM vegetarian LIMIT 3")
        data = c.fetchall()
        return data
    except Exception as e:
        messagebox.showerror("Error", f"Failed to retrieve restaurant data: {str(e)}")
        return []
    finally:
        if conn:
            conn.close()


# Function that allows for url to be opened in web broser
def open_url(url):
    webbrowser.open(url)


# Function to load image and for image resizing
def load_image(image_path, size=(346, 453)):
    # Check if the image file exists
    if not os.path.exists(image_path):
        messagebox.showerror("Error", f"Image file not found: {image_path}")
        return None

    try:
        # Attempt to open and resize the image
        img = Image.open(image_path)
        img = img.resize(size, Image.Resampling.LANCZOS)
        return ImageTk.PhotoImage(img)  # Returned resized image as a PhotoImage object
    except Exception as e:
        # Handle any exceptions that occur during image processing
        messagebox.showerror("Error", f"Failed to load image: {str(e)}")
        return None


# Initialize main window
window = Tk()
window.title("DINE-EZ")
window.geometry("1450x900")
window.configure(bg="#FFFFFF")


# Canvas setup to hold widgets
canvas = Canvas(window, bg="#FFFFFF", height=900, width=1450, bd=0, highlightthickness=0, relief="ridge")

canvas.place(x=0, y=0)


# Main function that loads and displays restaurant data
def main():
    restaurant_data = retrieve_restaurant_data()

    # Loading of images and URLs from main database
    images_and_urls = [(load_image(data[0]), data[1]) for data in restaurant_data]

    if not all(img for img, url in images_and_urls):
        return
    # Restaurant button 1, displays image button of the first restaurant and allows user to access restaurant website
    button_restaurant_1 = Button(image=images_and_urls[0][0], borderwidth=0, highlightthickness=0,
                                 command=lambda: open_url(images_and_urls[0][1]), relief="flat")
    button_restaurant_1.place(x=90.0, y=288.0, width=337.0, height=407.0)
    button_restaurant_1.image = images_and_urls[0][0]

    # Restaurant button 2, displays image button of the second restaurant and allows user to access restaurant website
    button_restaurant_2 = Button(image=images_and_urls[1][0], borderwidth=0, highlightthickness=0,
                                 command=lambda: open_url(images_and_urls[1][1]), relief="flat")
    button_restaurant_2.place(x=556.0, y=288.0, width=337.0, height=407.0)
    button_restaurant_2.image = images_and_urls[1][0]

    # Restaurant button 3, displays image button of the third restaurant and allows user to access restaurant website
    button_restaurant_3 = Button(image=images_and_urls[2][0], borderwidth=0, highlightthickness=0,
                                 command=lambda: open_url(images_and_urls[2][1]), relief="flat")
    button_restaurant_3.place(x=1022.0, y=288.0, width=337.0, height=407.0)
    button_restaurant_3.image = images_and_urls[2][0]


# Text to indicate Vegetarian options on the user interface
canvas.create_text(621.0, 220.0, anchor="nw", text="○ VEGETARIAN", fill="#000000", font=("Inter Light", 25))


# Dynamic text items for restaurant names on the canvas
# These placeholders will be updated with the real restaurant names from the database
restaurant_name_text_1 = canvas.create_text(125.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                            fill="#000000", font=("Inter Light", 25))
restaurant_name_text_2 = canvas.create_text(600.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                            fill="#000000", font=("Inter Light", 25))
restaurant_name_text_3 = canvas.create_text(1070.0, 713.0, anchor="nw", text="NAME OF RESTAURANT",
                                            fill="#000000", font=("Inter Light", 25))


# Disable window resizing on user interface
window.resizable(False, False)

# Main loop to run the application
if __name__ == "__main__":
    main()
window.mainloop()
