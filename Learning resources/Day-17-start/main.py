class User:
    # constructor
    def __init__(self, user_id, user_name):
        # initializes attributes
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1


user1 = User("01", "Rohan")
user2 = User("02", "Tahmid")

user2.follow(user1)
user1.follow(user2)

print(f"{user1.user_name}'s id is: {user1.id} and currently have {user1.followers} followers and following {user1.following} people.")
print(f"{user2.user_name}'s id is: {user2.id} and currently have {user2.followers} followers and following {user2.following} people.")


class Car:
    def __init__(self):
        self.seat = 5

    def enter_race_mode(self):
        self.seat = 2


car1 = Car()
print(car1.seat)

car1.enter_race_mode()
print(car1.seat)