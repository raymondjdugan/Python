# with open("weather_data.csv") as data_file:
#     data = data_file.readlines()
#     print(data)
# import csv
#
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temperatures = []
#     for row in data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))
#
#     print(temperatures)
import pandas

# data = pandas.read_csv("weather_data.csv")
# print(data["temp"])

# data_dict = data.to_dict()
# print(data_dict)
# temp_list = data["temp"].to_list()
# print(temp_list)

# Get column data
# print(f"The average temp for this list is {data.temp.mean()}")
# print(f"the max value in the list is {data['temp'].max()}")

# Get data in row
# print(data[data.temp == data.temp.max()])
# monday = data[data.day == "Monday"]
# print((monday.temp * 9/5) + 32)

# Create Dataframe From Scratch
# data_dict = {
#     "students": ["Amy", "James", "Angela"],
#     "scores": [76, 56, 65]
# }
# data = pandas.DataFrame(data_dict)
# data.to_csv("new_data.csv")

census_data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

gray_squirrels_count = len(census_data[census_data["Primary Fur Color"] == "Gray"])
red_squirrels_count = len(census_data[census_data["Primary Fur Color"] == "Cinnamon"])
black_squirrels_count = len(census_data[census_data["Primary Fur Color"] == "Black"])

squirrel_count_dict = {
    "Fur Color": ["gray", "red", "black"],
    "Count": [gray_squirrels_count, red_squirrels_count, black_squirrels_count]
}
squirrel_count = pandas.DataFrame(squirrel_count_dict)
squirrel_count.to_csv("squirrel_count")
