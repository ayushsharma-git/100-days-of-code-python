##################### Extra Hard Starting Project ######################
import datetime as dt
import random

import pandas as pd

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()

birthdays = pd.read_csv("birthdays.csv")
# print(birthdays)
birthday = birthdays.loc[
    (birthdays['year'] == now.year) & (birthdays['month'] == now.month) & (birthdays['day'] == now.day)]
# print(birthday['name'].item())
if not birthday.empty:
    file_name = "letter_templates/letter_" + str(random.randint(1, 3)) + ".txt"
    with open(file_name, mode="r") as file:
        pass
        content = file.read().replace("[NAME]", birthday['name'].item())
    print(content)

# print(birthday)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
