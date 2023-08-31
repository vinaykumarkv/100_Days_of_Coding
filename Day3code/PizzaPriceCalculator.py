# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S" and add_pepperoni == "Y" and extra_cheese =="Y":
    price= 15 + 2 + 1
elif size == "M" and add_pepperoni == "Y" and extra_cheese =="Y":
    price= 20+ 3+ 1
elif size == "L" and add_pepperoni == "Y" and extra_cheese =="Y":
    price= 25+ 3+ 1
elif size == "S" and add_pepperoni == "N" and extra_cheese =="Y":
    price=15+1
elif size == "M" and add_pepperoni == "N" and extra_cheese =="Y":
    price=20+1
elif size == "L" and add_pepperoni == "N" and extra_cheese =="Y":
    price=25+1
elif size == "S" and add_pepperoni == "N" and extra_cheese =="N":
    price=15
elif size == "M" and add_pepperoni == "N" and extra_cheese =="N":
    price=20
elif size == "L" and add_pepperoni == "N" and extra_cheese =="N":
    price=25
print(f"Your final bill is: ${price}.")
