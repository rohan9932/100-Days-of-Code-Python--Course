from tkinter import *


# functions
def calculate():
    mile = float(input.get())
    km = round(mile * 1.60934, 2)
    ans.config(text= km)


# make window
window = Tk()
window.title("Mile to KM Converter")
window.minsize(width= 200, height= 150)
window.config(padx= 30, pady= 30)

# Input
input = Entry(width= 10)
input.grid(column= 1, row= 0)

# Labels
miles = Label(text= "Miles")
miles.grid(column= 2, row= 0)

is_equal_to = Label(text= "is equal to")
is_equal_to.grid(column= 0, row= 1)

ans = Label(text= "0")
ans.grid(column= 1, row= 1)

km = Label(text= "Km")
km.grid(column= 2, row= 1)

# Button
calculate_btn = Button(text= "Calculate", command= calculate)
calculate_btn.grid(column= 1, row= 2)


window.mainloop()