import pandas

data = pandas.read_csv("Squirrel_Data.csv")
# colours = data["Primary Fur Color"].drop_duplicates().tolist()
# color_list = data["Primary Fur Color"].tolist()
# colour_counts = []
# print(colours)
# colours.remove([0])
#
# def compare_and_count(c, clrlist):
#     count = 0
#     for d in clrlist:
#         if c == d:
#             count += 1
#             print("found")
#     return count
#
#
# for color in colours:
#     colour_counts.append(compare_and_count(color, color_list))
#
# data_frame = {
#     "Fur Color": colours,
#     "Count": colour_counts
# }
grey_squirrels = len(data[data["Primary Fur Color"] == "Gray"])
red_squirrels = len(data[data["Primary Fur Color"] == "Cinnamon"])
black = len(data[data["Primary Fur Color"] == "Black"])

data_frame = {
     "Fur Color": ["Gray","Cinnamon","Black"],
     "Count": [grey_squirrels,red_squirrels,black]
}

cdata = pandas.DataFrame(data_frame)
cdata.to_csv("Squirrel_Count")
