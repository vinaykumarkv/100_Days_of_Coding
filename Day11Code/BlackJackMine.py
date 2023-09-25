import random



def calculator():
    cards = [11,2,3,4,5,6,7,8,9,10,10,10,10]
    decision = "1"
    c1=random.choice(cards)
    c2=random.choice(cards)
    c=c1+c2
    
    com1 = random.choice(cards)
    com2 = random.choice(cards)
    com=com1+com2
    print(f"your cards are {c1} {c2}")
    print(f"computer cards are {com1} {com2}")
    
    if c > 21 and com < 21:
        print(f"your score is {c}")
        print(f"computer score is {com}")
        return f"Computer is the winner!! {com}"
        
    elif c < 21 and com > 21:
        print(f"your score is {c}")
        print(f"computer score is {com}")
        return f"You are the winner!! {c}"
        
    elif c == 21:
        print(f"your score is {c}")
        print(f"computer score is {com}")
        return f"You are the winner!! Black Jack {c}"
    elif com == 21:
        print(f"your score is {c}")
        print(f"computer score is {com}")
        return f"Computer is the winner!! Black Jack{com}"
    else:
        pass
    decision = input("Do you want to Hit (1) or Hold (0):")
    while decision == "1":
        c3 = random.choice(cards)
        c = c+c3
        print(f"your next card is {c3}")
        if c >21:
            print(f"your score is {c}")
            print(f"computer score is {com}")
            return f"You Lose!! {c}"  
        else:
            pass
        com3 = random.choice(cards)
        com = com+com3
        print(f"your next card is {com3}")
        if com >21:
            print(f"your score is {c}")
            print(f"computer score is {com}")
            return f"You win!! {c}"  
        else:
            pass
        print(f"your score so far is {c}")
        print(f"computer score so far is {com}")
        decision = input("Do you want to Hit (1) or Hold (0):")
    
    print(f"your score is {c}")
    print(f"computer score is {com}")
    if c > com and c <= 21:     
        return "You Win!!"
    elif c < com and com <= 21:
        return "You Lose!!"
    
value=calculator()
print(value)
