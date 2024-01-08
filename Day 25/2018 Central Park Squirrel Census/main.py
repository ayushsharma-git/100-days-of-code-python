import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240108.csv")
# print(data.head(2))
# print(data.columns)
fur_colors_series = data["Primary Fur Color"]

# print(fur_colors_series)
# print(fur_colors_series.value_counts())

counts_by_fur = data.value_counts(subset="Primary Fur Color", dropna=True)
counts_by_fur.reindex()

print(counts_by_fur)
print(counts_by_fur.index.name)
series_indexes = counts_by_fur.index
print(type(series_indexes))

print(counts_by_fur.name)
print(counts_by_fur.iloc[0])
print(type(counts_by_fur))
counts_by_fur_list = counts_by_fur.to_list()
print("*************LIST*************")
print(counts_by_fur_list)

counts_by_fur_dict = counts_by_fur.to_dict()
print("*************DICT*************")
print(counts_by_fur_dict)
df = pandas.DataFrame(data=counts_by_fur_dict, index=["Count"])
print("*************DF*************")
print(df.T)
print(df.columns)
# df.to_csv("test.csv")
data = []
for key in counts_by_fur_dict:
    data.append([key, counts_by_fur_dict[key]])

df_new = pandas.DataFrame(data, index=None, columns=["Fur Color", "Count"])
print(df_new)
df_new.to_csv("test.csv")

# Central Park Squirrel Data Analysis

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240108.csv")
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(grey_squirrels_count)
print(red_squirrels_count)
print(black_squirrels_count)

data_dict = {
    "Fur Color": ["Gray", "Cinnamon", "Black"],
    "Count": [grey_squirrels_count, red_squirrels_count, black_squirrels_count]
}

df = pandas.DataFrame(data_dict)
df.to_csv("squirrel_count.csv")
