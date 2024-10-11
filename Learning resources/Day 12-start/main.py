################### Scope ####################

# enemies = 1

# def increase_enemies():
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

# increase_enemies()
# print(f"enemies outside function: {enemies}")

#Local Scope
def game():
    strength = 5
    print(strength) #this variable is accessable only inside of the function because it's a local variable

game()
# print(strength)

#Global Scope
strength = 50

def game_2():
    def game_nested():
      print(strength) #this variable can be accessable from anywhere in the file because it's a global variable
    game_nested()

game_2()
print(strength)

#There is no block scope
#It means there is no local scope for in blocks of if, elif, for etc. loops

game_level = 2
players = ["Shakib", "Tamim", "Mahmudullah"]

if game_level < 5:
   new_opponent = players[0]

print(new_opponent) #this will get printed because there are no local scope for conditional statements blocks

#Modifying global scopes
enemies = 1

# def increase_enemies():
#   global enemies #defines that there is a global variable named enemies somewhere in the file
#   enemies = 2
#   print(f"enemies inside function: {enemies}")

def increase_enemies():
   return enemies + 1

enemies = increase_enemies()
print(f"enemies outside function: {enemies}")

#Global Constants

PI = 3.1416
print(PI)