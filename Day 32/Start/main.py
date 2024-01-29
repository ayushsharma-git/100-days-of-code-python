import datetime as dt
import random


# my_email = "test@test.com"
# password = "ASDF"
#
# with smtplib.SMTP("smtp.gmail.com") as connection:
#     connection.starttls()
#     connection.login(user=my_email, password=password)
#     connection.sendmail(from_addr=my_email, to_addrs="abc@test.com",
#                         msg="Subject:Hello\n\nThis is the body of my email")

def get_quote():
    with open("quotes.txt", mode="r") as file:
        quotes = file.readlines()
    return random.choice(quotes)


now = dt.datetime.now()

if now.weekday() == 0:
    print(get_quote())
