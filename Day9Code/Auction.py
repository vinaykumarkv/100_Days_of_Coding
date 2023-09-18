from turtle import clear

print("""
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                         `'-------'`
                       .-------------.
                      /_______________\\
             
 
                      
 Welcome to secret auction program!""")
bidders="yes"
auction= {}
while bidders=="yes":
    name = input("What is your name?: ")
    bid = int(input("What is your bid amount?: $ "))
    auction[name]=bid
    bidders = input ("Are there any other bidders?(yes or no): ")

print(auction)
temp =0
for name in auction:
    if auction[name]> temp:
        temp = auction[name]
        winner = name
    else:
        pass

clear()
print(f"The winner is {winner} with a bid of ${temp}.")    

    
