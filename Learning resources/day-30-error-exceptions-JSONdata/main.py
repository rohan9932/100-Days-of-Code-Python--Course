# File Not Found
# with open("hello.txt") as f:
#     f.read()

# KeyError
# a_dict = {"key": "value"}
# value = a_dict["non_existent_key"]

# IndexError
# fruit_list = ["Apple", "Banana", "Grapes"]
# fruit = fruit_list[3]

# TypeError
# text = "hello"
# print(text + 5)

'''
try: Something that might cause an exception
except: Do this if there was an exception
else: Do this if there were no exceptions
finally: Do this no matter what happens
raise: Raise our own exception
'''

# try:
#     file = open("a_file.txt")
#     a_dict = {"key": "value"}
#     value = a_dict["key"]
#     print(value)
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Hello")
# except KeyError as error_message:
#     print(f"The key {error_message} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File was closed.")
#     raise KeyError("This is an personal made up error")

# use case of raise
height = float(input("Enter your height(m): "))
weight = float(input("Enter your weight(kg): "))

if height > 3:
    raise ValueError("Human height cannot exceed over 3 meters.")

bmi = weight / height ** 2
print(bmi)
