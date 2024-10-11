import turtle as trt
import random


arrow = trt.Turtle()
trt.colormode(255)
arrow.shape("classic")
# arrow.width(15)

#
# # defining shapes
# def triangle():
#     for i in range(3):
#         arrow.bk(100)
#         arrow.left(120)
#
#
# def square():
#     for i in range(4):
#         arrow.bk(100)
#         arrow.left(90)
#
#
# def pentagon():
#     for i in range(5):
#         arrow.bk(100)
#         arrow.left(72)
#
#
# def hexagon():
#     for i in range(6):
#         arrow.bk(100)
#         arrow.left(60)
#
#
# def heptagon():
#     for i in range(7):
#         arrow.bk(100)
#         arrow.left(51.42)
#
#
# def octagon():
#     for i in range(8):
#         arrow.bk(100)
#         arrow.left(45)
#
#
# def nonagon():
#     for i in range(9):
#         arrow.bk(100)
#         arrow.left(40)
#
#
# def decagon():
#     for i in range(10):
#         arrow.bk(100)
#         arrow.left(36)
#
#
#
# arrow.color(random.choice(color))
# triangle()
# arrow.home()
# arrow.color(random.choice(color))
# square()
# arrow.home()
# arrow.color(random.choice(color))
# pentagon()
# arrow.home()
# arrow.color(random.choice(color))
# hexagon()
# arrow.home()
# arrow.color(random.choice(color))
# heptagon()
# arrow.home()
# arrow.color(random.choice(color))
# octagon()
# arrow.home()
# arrow.color(random.choice(color))
# nonagon()
# arrow.home()
# arrow.color(random.choice(color))
# decagon()
# arrow.home()



# for i in range(15):
#     arrow.fd(10)
#     arrow.up()
#     arrow.fd(10)
#     arrow.down()


# color = ["AliceBlue", "CadetBlue2", "DarkSalmon", "DeepSkyBlue", "burlywood2", "aquamarine2", "DarkOrange", "bisque2",
#          "BlanchedAlmond", "DarkSeaGreen2"]


# def draw_shape(num_of_side):
#     angle = 360 / num_of_side
#     for i in range(num_of_side):
#         arrow.bk(100)
#         arrow.left(angle)
#
#
# for shape_side in range(3, 11):
#     arrow.color(random.choice(color))
#     draw_shape(shape_side)

# directions = [0, 90, 180, 270]
arrow.speed("fastest")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


# for i in range(300):
#     arrow.color(random_color())
#     arrow.fd(50)
#     arrow.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    num_of_circles = int(360 / size_of_gap)
    for i in range(num_of_circles):
        arrow.color(random_color())
        arrow.circle(100)
        current_heading = arrow.heading()
        arrow.setheading(current_heading + size_of_gap)


draw_spirograph(2)

screen = trt.Screen()
screen.exitonclick()
