# default argument values
def func(a= 1, b= 2, c= 3):
    print(a, b, c)

func(b= 5)

# unlimited positional arguments
def add(*args):
    sum = 0
    for n in args: # can loop through args which is stored as a tuple
        sum += n
    return sum

print(add(5, 7, 9, 10, 24, 35))

# unlimited keyword arguments
def calculator(n, **kwargs): # kwargs is stored as a dictionary
    n += kwargs["add"] # n(5) + 5 = 10
    n *= kwargs["multiply"] # n(10) * 10 = 100
    print(n)

calculator(5, add= 5, multiply= 10)

class Car:
    def __init__(self, **kwargs):
        self.car = kwargs.get("car")
        self.model = kwargs.get("model") # works same as dict[key] but diff is won't give error and return none if there is no value
        self.color = kwargs.get("color")

car = Car(make= "Lamborghini", model= "Urus")
print(car.color)
