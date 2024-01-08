import pandas

# with open("weather_data.csv") as data_file:
#     weather_data = data_file.readlines()


# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != 'temp':
#             temperatures.append(int(row[1]))
#     print(temperatures)

data = pandas.read_csv("weather_data.csv")
print(data)
data_dict = data.to_dict()
temp_list = data["temp"].to_list()

# series 1D
# data frame 2D

# avg = sum(temp_list) / len(temp_list)
print(data["temp"].mean())
print(data.temp.max())
print(data[data.temp == data.temp.max()])
