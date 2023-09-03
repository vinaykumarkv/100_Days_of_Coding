R = input("Type in the range (From, To) : ")
R = R.split(", ")
R1 = int(R[0])
R2 = 1 + int(R[1])
i=0
for S in range(R1,R2):
    if int(S)%3 == 0 and int(S)%5 == 0:
        print("FizzBuzz")
    elif int(S)%3 == 0:
        print("Fizz")
    elif int(S)%5 == 0:
        print("Buzz")
    else:
        print(int(S))
        continue
