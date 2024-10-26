# File I/O

# file = open(file= "my_file.txt")
# contents = file.read()
# print(contents)
# file.close()

# or
# with open(file="/Users/01rohan/Desktop/my_file.txt", mode="r") as file:
#     contents = file.read()  # read the file and save the written texts as "string"
#     print(contents)

# with open(file= "new_file.txt", mode= "w") as n_file:
#     n_file.write("New file!")

with open(file="my_file.txt", mode="r") as file:
    contents = file.read().splitlines()  # read the file and save the written texts as "string"
    print(contents)


