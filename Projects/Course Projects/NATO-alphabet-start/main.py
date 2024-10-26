import pandas as pd


#TODO 1. Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
data = pd.read_csv("nato_phonetic_alphabet.csv")
# making a dict from data like " {"A": "Alfa", "B": "Bravo"} " format
data_dict = {row.letter: row.code for (index, row) in data.iterrows()}

#TODO 2. Create a list of the phonetic code words from a word that the user inputs.
continue_loop = True
while continue_loop:
    user_input = input("Enter a word: ").upper()
    try:
        # loop through the user input and output the data_dict[letter]
        output_list = [data_dict[letter] for letter in user_input]
    except KeyError:
        print("Sorry! Only letters in the alphabet please.")
    else:
        print(output_list)
        continue_loop = False
