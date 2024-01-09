import random

import pandas

# Looping through lists
names = ["Roger", "Nadal", "Novac", "Andre", "Sarena", "Mariya", "Martina"]

for name in names:
    print(name)
names_new_list = [name for name in names if len(name) > 3]
# Looping through lists
person = {"name": "Jessa", "country": "USA", "telephone": 1178}

for (key, value) in person.items():
    print(f"{key}:{value}")

person_new_dict = {key: value for (key, value) in person.items() if value is not None}

for key in person:
    value = person[key]
    print(f"{key}:{value}")
print("****************************")
names = ["Alex", "Beth", "Caroline", "Dave", "Elanor", "Freddie"]
scores = [random.randint(1, 100) for name in names]
student_dict = {"student": names, "scores": scores}
student_grades_df = pandas.DataFrame(student_dict)
print(student_grades_df)
# Loop through a dataframe
for (label, value) in student_grades_df.items():
    print(f"Label(columns):\n{label}")
    print(f"Value(Series):\n{value}")
# Iterate through a dataframe
print("Iterate through a dataframe")
for (index,row) in student_grades_df.iterrows():
    print(row.student)
    print(row.scores)