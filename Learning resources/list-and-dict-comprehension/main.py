# List comprehension

#eg 
numbers = [1, 2, 3]
new_numbers = []
for n in numbers:
    add1 = n + 1
    new_numbers.append(add1)
# or
numbers = [1, 2, 3]
# new_list = [new_item for item in list]
new_numbers = [n + 1 for n in numbers]

# Conditional list comprehension
# new_item = [new_item for item in list if test]
#eg
names = ["Rohan", "Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
short_names = []
for name in names:
    if len(name) < 6:
        short_names.append(name)
# or,
short_names = [name for name in names if len(name) < 6]


# Dictionary comprehension

# new_dict = {new_key: new_value for item in list}
# new_dict = {new_key: new_value for (key, value) in dict.items()}
# new_dict = {new_key: new_value for (key, value) in dict.items() if test}


# pandas dataframe iteration
student_dict = {
    "student": ["Rohan", "Alex", "Hailey"],
    "score": [50, 57, 23]
}
# Looping through dictionary
for (key, value) in student_dict.items():
    print(value)

import pandas as pd
student_data_frame = pd.DataFrame(student_dict)
print(student_data_frame)

# Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    if row.student == "Rohan":
        print(row.score)

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}
