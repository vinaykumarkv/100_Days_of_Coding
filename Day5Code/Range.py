SetTheRange = input("Please type in the Range:(From, To, Steps) (Ex: 2, 10, 1): ")
SetTheRange = SetTheRange.split(", ")
R1 = int(SetTheRange[0])
R2 = 1 + int(SetTheRange[1])
Step = int(SetTheRange[2])
i=0
for S in range(R1,R2,Step):
    i += S
print(i)

