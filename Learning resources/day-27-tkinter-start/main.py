from tkinter import *


def button_clicked():
    new_text = input.get()
    my_label.config(text= new_text)


window = Tk()
window.title("First GUI")
window.minsize(width= 500, height= 300)
window.config(padx= 50, pady= 50)

# In tkinter we first have to make a component and then we have to specify where we want to show it on the screen.

# Label
my_label = Label(text= "First Label", font= ("Roboto", 19, "bold"))
# my_label.pack() # this method automatically centers the item on the screen
my_label.grid(column= 0, row= 0) # another layout manager and it's column and row is relative to other widgets
my_label.config(padx= 10, pady= 10) # padding around a specific widget

# can't use grid and pack in same program

# Button
button = Button(text= "Click Me", command= button_clicked) # command keyword works as a event listener
# button.pack() # it's one of the layout manager
button.grid(column= 1, row= 1)

# New Button
new_button = Button(text= "New Button")
new_button.grid(column= 2, row= 0)

# Entry
input = Entry(width= 10)
# input.place(x= 200, y= 300) # another layout manager
input.grid(column= 3, row= 2)



window.mainloop()