#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

# open the starting_letter.txt and invited_name.txt to generate letter template and make a list of invited members
with open(file= "./Input/Letters/starting_letter.txt", mode= "r") as letter:
    starting_letter = letter.read() # letter template

with open(file= "./Input/Names/invited_names.txt", mode= "r") as names_file:
    name_list = [] # list of the names of invited people
    names = names_file.readlines()
    # removing \n from the list names
    for name in names:
        updated_name = name.strip("\n")
        name_list.append(updated_name)

# this loop will create and write a customed file for each member in invited members list
for name in name_list:
    with open(file= f"./Output/ReadyToSend/letter_for_{name}.txt", mode= "w") as output:
        new_letter = starting_letter.replace("[name]", f"{name}")
        output.write(new_letter)