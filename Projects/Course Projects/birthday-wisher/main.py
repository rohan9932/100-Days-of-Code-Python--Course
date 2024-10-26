import pandas as pd
import datetime as dt
import random
import smtplib

# Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.day, now.month)

data = pd.read_csv("birthdays.csv")
birthdays_dict = {(data_row.day, data_row.month): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    birthday_person = birthdays_dict[today]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"

    # If true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    with open(file_path, "r") as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    # Send the letter generated in step 3 to that person's email address.
    my_email = "test.rohan932@gmail.com"
    password = "sutaqythfkmgsaku"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )
