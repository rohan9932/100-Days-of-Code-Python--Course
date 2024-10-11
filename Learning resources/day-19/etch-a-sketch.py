from turtle import Turtle, Screen

arrow = Turtle()
screen = Screen()

def move_forward():
    arrow.fd(20)

def move_backward():
    arrow.bk(20)

def move_left():
    arrow.left(10)

def move_right():
    arrow.right(10)

def clear_drawing():
    arrow.reset()



screen.listen()
screen.onkey(fun=move_forward, key="w")
screen.onkey(fun=move_backward, key="s")
screen.onkey(fun=move_left, key="a")
screen.onkey(fun=move_right, key="d")
screen.onkey(fun=clear_drawing, key="c")

screen.exitonclick()