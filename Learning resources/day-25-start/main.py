# # with open(file= "weather_data.csv", mode= "r") as data_file:
# #     data = data_file.readlines()
# #     print(data)
#
# # import csv
# #
# # with open(file= "weather_data.csv") as data_file:
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperature = int(row[1])
# #             temperatures.append(temperature)
# #
# #     print(temperatures)
#
# import pandas as pd

# data = pd.read_csv("weather_data.csv")
# # print(data)
# # #
# data_dict = data.to_dict()
# print(data_dict)
# #
# temp_data = data["temp"] # data series
# print(temp_data.mean())
# #
# # max_val = temp_data.max()
# # print(max_val)
# #
# # # print(temp_data)
# # temp_list = temp_data.tolist()
# # print(temp_list)
# # print(len(temp_list))
# #
# #
# # # print(type(data))
# #
# # # # making avg temp
# # # avg_temp = sum(temp_list) / len(temp_list)
# # # print(avg_temp)
# #
# #
# Get data in columns
# days = data["day"]
# print(days)
# # or
#
# print(days.tolist())

#
#
# # Get data in row
# # row = data[data.day == "Wednesday"]
# # print(row)
#
# # challenge
# highest_temp = data.temp.max()
# row = data[data.temp == highest_temp]
# print(row)
#
# monday = data[data.day == "Monday"]
# temp_in_C = monday.temp[0]
# temp_in_F = (9*temp_in_C / 5) + 32
# print(temp_in_F)
#
# # Creating a new DataFrame
# data_dict = {
#     "students": ["Rohan", "Tahmid", "Adib",],
#     "numbers": [25, 34, 39,],
# }
# act_data = pd.DataFrame(data_dict)
# print(act_data)
# act_data.to_csv("new_data.csv")

import pandas as pd

raw_data = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

raw_data_colors = raw_data["Primary Fur Color"].tolist()
# colors list
colors = pd.Series(raw_data_colors).drop_duplicates().tolist()[1:] # Series is a class in which drop_duplicates is a
# method to remove duplicate items in list.

counts = []

for color in colors:
    squirrels_count = len(raw_data[raw_data["Primary Fur Color"] == color])
    counts.append(squirrels_count)

# make new table
squirrel_count_dict = {
    "Fur Color": colors,
    "Count": counts,
}

squirrel_count = pd.DataFrame(squirrel_count_dict)
print(squirrel_count)

squirrel_count.to_csv("squirrel_count.csv")
