import random

def title():
    print("""
                                                                                             
88          88                       88        88                       88         
88          88                       88        ""                       88         
88          88                       88                                 88         
88,dPPYba,  88 ,adPPYYba,  ,adPPYba, 88   ,d8  88 ,adPPYYba,  ,adPPYba, 88   ,d8   
88P'    "8a 88 ""     `Y8 a8"     "" 88 ,a8"   88 ""     `Y8 a8"     "" 88 ,a8"    
88       d8 88 ,adPPPPP88 8b         8888[     88 ,adPPPPP88 8b         8888[      
88b,   ,a8" 88 88,    ,88 "8a,   ,aa 88`"Yba,  88 88,    ,88 "8a,   ,aa 88`"Yba,   
8Y"Ybbd8"'  88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a 88 `"8bbdP"Y8  `"Ybbd8"' 88   `Y8a  
                                              ,88                                  
                                            888P"                                  """)


def deal():
    cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
    return random.choice(cards)

def calculateScore(list):
 #   sum = 0
 #   for i in range (len(list)):
#        sum += int(list[i])
 #   return sum
    
    if sum(list) ==21  and len(list) ==2:
        return 0
    if 11 in list  and sum(list)>21:
        list.remove(11)
        list.append(1)
        
    return sum(list)

def compare(userScore,computerScore):
    if userScore == computerScore:
        return "Draw"
    elif userScore == 0:
        return "you Win with Black Jack!"
    elif computerScore == 0:
        return "Lose! computer wins with Black Jack"
    elif userScore > 21:
        return " you went over and Lose! computer wins"
    elif computerScore > 21:
        return "You Win! computer went over"
    elif userScore > computerScore:
        return "You Win! computer score is less"
    else:
        return "You Lose! computer score is more"
            
def playGame():
    title()
    userCards = []
    computerCards =[]
    isGameOver = False
    for i in range (2):
        userCards.append(deal())
        computerCards.append(deal())
        
    
    
    
    while not isGameOver:
        userScore = calculateScore(userCards)
        computerScore = calculateScore(computerCards)
        
        print(f"your card: {userCards} and your score: {userScore}")
        print(f"Computer's 1st card: {computerCards[0]}")
        
        if userScore == 0 or computerScore ==0 or userScore >21:
            isGameOver = True
        else:
            userDeal = input("Type 'y' to get another card, type 'n' to pass: ")
            if userDeal =='y':
               userCards.append(deal())
            else:
                isGameOver = True
        
    while computerScore != 0 and computerScore<17:
        computerCards.append(deal())
        computerScore = calculateScore(computerCards)
    
    print(f"your card: {userCards} and your score: {userScore}")
    print(f"Computer's card: {computerCards} and Computer score: {computerScore}")
    print(compare(userScore,computerScore))    
    
while input("Do you want to play game BlackJack?? type 'y' or 'n' :") == "y":
    playGame()
    