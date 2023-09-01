import random

peep = input("Type in all the names saperated by commas who wants to participate in split the bill: ")
pep =peep.split(", ")
print (pep)
rpep = random.choice(pep)
print(f"The person to pay the bill is : {rpep}")

#the other way could be
plen= len(pep)
print(plen)
rpos = random.randint(0,plen-1)
print(f"The person to pay the bill is : {pep[rpos]}")
