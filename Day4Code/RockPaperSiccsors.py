import random

gamechoice = ["rock","paper","scissors"]
rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")
paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")
scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

yourturn = input ("whats your go is it rock, paper or scissors? ")

if yourturn == "rock":
    print(rock)
elif yourturn == "paper":
    print(paper)
else:
    print(scissors)

compturn = random.choice(gamechoice)

if compturn == "rock":
    print(rock)
elif compturn == "paper":
    print(paper)
else:
    print(scissors)
    
if yourturn == compturn:
    print("its a tie!")
elif yourturn == "rock" and compturn == "paper":
    print("computer wins! rock is covered by paper.")
elif yourturn == "paper" and compturn == "scissors":
    print("computer wins! paper is cut by scissors.")
elif yourturn == "scissors" and compturn == "rock":
    print("computer wins! rock damaged your scissors.")
elif yourturn == "paper" and compturn == "rock":
    print("you win! rock is covered by paper.")
elif yourturn == "scissors" and compturn == "paper":
    print("You win! paper is cut by scissors.")
elif yourturn == "rock" and compturn == "scissors":
    print("You win! rock damaged scissors.")