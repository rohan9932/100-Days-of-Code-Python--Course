from tkinter import *
import pandas as pd
import random

BACKGROUND_COLOR = "#B1DDC6"

# --------------- HANDLING DATA -------------- #
to_learn = {}
current_card = {}

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words.csv")
    to_learn = original_data.to_dict("records")
else:
    to_learn = data.to_dict("records")


def next_card():
    global current_card, flip_timer
    screen.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    de_word = current_card["German"]
    card.itemconfig(card_background, image= card_front)
    card.itemconfig(title_txt, text= "German", fill= "black")
    card.itemconfig(word_txt, text= de_word, fill= "black")
    flip_timer = screen.after(3000, flip_card)


def flip_card():
    eng_word = current_card["English"]
    card.itemconfig(card_background, image= card_back)
    card.itemconfig(title_txt, text= "English", fill= "white")
    card.itemconfig(word_txt, text= eng_word, fill= "white")


def is_known():
    to_learn.remove(current_card)
    data = pd.DataFrame(to_learn)
    data.to_csv("data/words_to_learn.csv", index= False)
    next_card()


# --------------- UI SETUP ------------------- #
screen = Tk()
screen.title("Flash Card")
screen.config(padx= 50, pady= 50, bg= BACKGROUND_COLOR)
flip_timer = screen.after(3000, func= flip_card)

# card canvas
card = Canvas(width= 800, height= 526, bg= BACKGROUND_COLOR, highlightthickness= 0)
card_front = PhotoImage(file= "images/card_front.png")
card_back = PhotoImage(file= "images/card_back.png")
card_background = card.create_image(400, 263, image= card_front)
title_txt = card.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill= "black")
word_txt = card.create_text(400, 263, text="", font=("Ariel", 60, "bold"), fill= "black")
card.grid(row= 0, column= 0, columnspan= 2)

# buttons
cross_img = PhotoImage(file= "images/wrong.png")
cross_btn = Button(image= cross_img, highlightthickness= 0, borderwidth= 0, relief= "flat",
                   activebackground= BACKGROUND_COLOR, highlightbackground= BACKGROUND_COLOR,
                   highlightcolor= BACKGROUND_COLOR, command= next_card)
cross_btn.grid(row= 1, column= 0)
tick_img = PhotoImage(file= "images/right.png")
tick_btn = Button(image= tick_img, highlightthickness= 0, borderwidth= 0, relief= "flat",
                  activebackground= BACKGROUND_COLOR, highlightbackground= BACKGROUND_COLOR,
                  highlightcolor= BACKGROUND_COLOR, command= is_known)
tick_btn.grid(row= 1, column= 1)

next_card()

screen.mainloop()
