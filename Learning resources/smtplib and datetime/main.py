# import smtplib # Simple Mail Transfer Protocol Library
#
# my_email = "test.rohan932@gmail.com"
# password = "sutaqythfkmgsaku"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls() # TLS stands for Transport Layer Security which encrypts email
#     connection.login(user= my_email, password= password)
#     connection.sendmail(
#         from_addr= my_email,
#         to_addrs= "t.mail932@yahoo.com",
#         msg= "Subject:Hello\n\nBody."
#     )
#

# import datetime as dt
#
# now = dt.datetime.now()
# year = now.year
# day = now.day
# day_of_week = now.weekday() # the x'th week
# print(year)
# print(day)
# print(day_of_week)
#
# date_of_birth = dt.datetime(year=2004, month=10, day=11, hour=16 )
# print(date_of_birth)

import smtplib
import datetime as dt
import random

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 3:
    with open(file="quotes.txt", mode="r") as quotes_file:
        quotes = quotes_file.read().splitlines()

    random_quote = random.choice(quotes)

    my_email = "test.rohan932@gmail.com"
    password = "sutaqythfkmgsaku"
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user= my_email, password= password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="t.mail932@yahoo.com",
            msg=f"Subject:Quote\n\n{random_quote}"
        )



