Heights = input ("Provide Heights in cms saperated by commas (example: 153, 123, 145..): ")
Height = Heights.split(", ")
S = 0
for H in Height:
    print(int(H))
    S += int(H)
Avg = S/len(Height)
print(f"Average Hieght is : {round(Avg)}")
