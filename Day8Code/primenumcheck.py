import math

def primecheck(n):
    flag = 0
    for i in range (2, n):
        if n % i == 0:
            flag = 1
        else:
            pass
    if flag ==1:
        print(f"{n} is not a prime number")
    else:
        print(f"{n} is a prime number")
        
num = int(input("Please provide the number to check if its prime number: "))
primecheck(num)
