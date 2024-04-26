from tkinter import *
import pandas
import csv
import random
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

# ----------------------Function to read CSV and make Data frame to access data----------------------
code_data_frame = pandas.read_csv("data/french_words.csv")
code_dict = code_data_frame.to_dict(orient="records")
known_dict = []


def know_the_word():
    code_dict.remove(current_card)
    data = pandas.DataFrame(code_dict)
    data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ---------------------Function to skip if you remember or not-----------------------
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(code_dict)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    window.after(3000, func=flip_card)


def flip_card():
    canvas.itemconfig(canvas_title, text="English")
    canvas.itemconfig(canvas_word, text=current_card["English"])
    canvas.itemconfig(canvas_img, image=card_back)


# -----------------UI Code-------------------
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=next_card)

canvas = Canvas(height=526, width=800)
card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas_img = canvas.create_image(400, 263, image=card_front)
canvas_title = canvas.create_text(400, 150, text="Title", font=("Arial", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="Word", font=("Arial", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=know_the_word)
right_button.grid(row=1, column=0)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=1)

mainloop()
