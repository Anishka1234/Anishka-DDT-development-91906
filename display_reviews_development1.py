# Imports
from pathlib import Path
import sqlite3
from tkinter import Tk, Canvas, Button, PhotoImage


# Paths set for assets and outputs
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("display_reviews")


# Function to retrieve the path to an asset
def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


# Initialize main window
window = Tk()
window.geometry("800x446")
window.configure(bg="#FFFFFF")


# Canvas setup to hold widgets
canvas = Canvas(
    window,
    bg="#FFFFFF",
    height=446,
    width=800,
    bd=0,
    highlightthickness=0,
    relief="ridge"
)

canvas.place(x=0, y=0)


canvas.create_text(350.0, 72.0, anchor="nw", text="REVIEWS", fill="#000000", font=("Inter ExtraLightItalic", 20))


# Create text items for displaying reviews
text_id1 = canvas.create_text(104.0, 117.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id2 = canvas.create_text(104.0, 150.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id3 = canvas.create_text(104.0, 183.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id4 = canvas.create_text(104.0, 216.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id5 = canvas.create_text(104.0, 249.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id6 = canvas.create_text(104.0, 281.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id7 = canvas.create_text(104.0, 313.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id8 = canvas.create_text(104.0, 376.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id9 = canvas.create_text(104.0, 403.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id10 = canvas.create_text(104.0, 347.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))

# List of text item IDs for reviews
text_ids = [text_id1, text_id2, text_id3, text_id4, text_id5, text_id6, text_id7, text_id8, text_id9, text_id10]


# Create text items for displaying usernames
text_id11 = canvas.create_text(
    35.0, 117.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))

text_id12 = canvas.create_text(
    35.0,
    150.0,
    anchor="nw",
    text="",
    fill="#000000",
    font=("Inter", 15 * -1)

)

text_id13 = canvas.create_text(35.0, 183.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id14 = canvas.create_text(35.0, 216.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id15 = canvas.create_text(35.0, 249.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id16 = canvas.create_text(35.0, 281.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id17 = canvas.create_text(35.0, 313.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id18 = canvas.create_text(35.0, 376.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id19 = canvas.create_text(35.0, 404.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))
text_id20 = canvas.create_text(35.0, 347.0, anchor="nw", text="", fill="#000000", font=("Inter", 15))


# List of text item IDs for usernames
text_ids = [text_id11, text_id12, text_id13, text_id14, text_id15, text_id16,
            text_id17, text_id18, text_id19, text_id20]


# Disable window resizing on user interface
window.resizable(False, False)
window.mainloop()
