# inheritence
class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print(f"Inhale, Exhale!")

class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("doing this underwater.")

    def swim(self):
        print(f"Moving in water.")


nemo = Fish()
nemo.swim()
nemo.breathe()


# slicing
piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "me", "fa", "so", "la", "ti")

print(piano_keys[::-1])
print(piano_tuple[::-1])