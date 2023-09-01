row1= ["🀢","🀢","🀢"]
row2= ["🀢","🀢","🀢"]
row3= ["🀢","🀢","🀢"]
map1= [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input ("please choose you position, where you want to place your treasure in row,column form \n(i.e, ex: 2,3) \n(0,0) (0,1) (0,2)\n(1,0) (1,1) (1,2)\n(2,0) (2,1) (2,2)\n\n:")
split1 = position.split(",")
r = int(split1[0])
c = int(split1[1])
print(f"{r},{c}")
map1[r][c] = "💰"
print(f"{map1[0]}\n{map1[1]}\n{map1[2]}")

