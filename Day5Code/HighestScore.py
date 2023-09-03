Score = input("Type in the scores in whole number and saperated by commas (ex: 23, 45, 67 ..):  ")
Score = Score.split(", ")
i = 0
for H in Score:
    if i < int(H):
        i = int(H)
    elif i == int(H):
        i = int(H)
    else:
        continue
print(f"The highest score is : {i}")