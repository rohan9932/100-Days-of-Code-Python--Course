# ********Day 54 Start**********
# Functions can have inputs/functionality/output
# def add(n1, n2):
#     return n1 + n2
#
# def subtract(n1, n2):
#     return n1 - n2
#
# def multiply(n1, n2):
#     return n1 * n2
#
# def divide(n1, n2):
#     return n1 / n2

##Functions are first-class objects, can be passed around as arguments e.g. int/string/float etc.
# def calculate(calc_func, n1, n2):
#     return calc_func(n1, n2)

# print(calculate(multiply, 5, 10))

# Nested functions
# def outer_func():
#     print("7")
#
#     def inner_func():
#         print("5")
#     inner_func()
#
# outer_func()

# Functions can be returned from other functions
# def outer_function():
#     print("I'm outer")
#
#     def nested_function():
#         print("I'm inner")
#
#     return nested_function # brackets activates the function
#
# inner_function = outer_function()
# inner_function()

# Python Decorator

import time

def delay_decorator(func):
    def wrapper_func():
        time.sleep(2)
        func()
    return wrapper_func

@delay_decorator
def say_hello():
    print("Hello!")

def greetings():
    print("How do you do?")

def say_bye():
    print("Bye!")

say_hello()
greetings()
say_bye()

# Advanced decorators
class User:
    def __init__(self, name):
        self.name = name
        self.is_logged_in = False

def authentication_check_decorator(func):
    def wrapper_func(*args, **kwargs):
        if args[0].is_logged_in == True:
            func(args[0])
    return wrapper_func

@authentication_check_decorator
def create_a_post(user):
    print(f"This is {user.name}'s new post.")

new_user = User("Rohan")
new_user.is_logged_in = True
create_a_post(new_user)

