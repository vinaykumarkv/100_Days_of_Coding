import random
import string

a2z = string.ascii_uppercase
a2z = [*a2z]
print(a2z)
n =  [str(i) for i in range(1,10)]
n = [*n]

print(n)
Sy = string.punctuation
Sy = [*Sy]
print(Sy)
passwd = ""
print("Welcome to the password generator!!")
la = int(input("number of alphabets in your password? : \n"))
lnum = int(input("number of numerics in your password? : \n"))
ls = int(input("number of Special characters in your password? : \n"))
for i in range(la):
    passwd = passwd+(random.choice(a2z))
    print(passwd)
for j in range(lnum):
    passwd = passwd+(random.choice(n))
    print(passwd)
for j in range(ls):
    passwd = passwd+(random.choice(Sy))
    print(passwd)
passwd = [*passwd]  
random.shuffle(passwd)
passwd=''.join(passwd)
print(passwd)
