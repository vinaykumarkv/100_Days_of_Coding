# import csv
# with open("weather_data.csv") as data_file:
#     data = csv.reader(data_file)
#     temp = []
#     for row in data:
#         if row[1] != "temp":
#             temp.append(int(row[1]))
#     print(temp)

import pandas
# data = pandas.read_csv("weather_data.csv")
# data_list = data["temp"].tolist()
# print(sum(data_list)/len(data_list))
# print(data["temp"].mean())
# print(data["temp"].max())
# print(data.temp)
# print(data[data.temp == data.temp.max()])

data_dict ={
    "students": ["Amy","James","Angela"],
    "Scores": ["76","56","65"]
}
data = pandas.DataFrame(data_dict)
print(data)
data.to_csv("New_File.csv")