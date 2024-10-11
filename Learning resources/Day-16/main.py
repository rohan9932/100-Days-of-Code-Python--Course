# from turtle import Turtle, Screen
#
# timmy = Turtle()
# print(timmy)
# timmy.shape("turtle")
# timmy.color("aquamarine3")
# timmy.fd(100)
#
# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import *
table = PrettyTable()
table.add_column("Pokemon name", ["Pikachu", "Squirtle", "Charmandar"])
table.add_column("Type", ["Electric", "Water", "Fire"])

table.valign = "m"
table.align = "l"


print(table)