import string

print("""
           88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88        |"""      )

eORd =""
eORd = str.lower(input("Do you want to enocode or decode? - "))
while eORd not in {"encode","decode"}:
    print("incorrect selection for encode/decode. please select right option")
    eORd = input("Do you want to enocode or decode? - ")
else:
    pass

message = str.lower(input ("Please input the message: "))

shift = int(input("Please provide the shift number - "))

def encode(e,s):
    a2z = string.ascii_lowercase[::]
    t = ""
    for i in range (len(e)):
        for j in range(len(a2z)):
            if e[i]==a2z[j]:
                if (j+s) > 25:
                    r = (j+s)-25                    
                else:
                    r = j+s
                t = t+a2z[r]
                print(t)
            else:
                pass
    print (t)
    

def decode(e,s):
    a2z = string.ascii_lowercase[::]
    t = ""
    for i in range (len(e)):
        for j in range(len(a2z)):
            if e[i]==a2z[j]:
                if (j-s) < 0:
                    r = 25 + j -s                   
                else:
                    r = j-s
                t = t+a2z[r]
                print(t)
            else:
                pass
    print (t)


if eORd == "encode":
    encode(message,shift)
elif eORd == "decode":
    decode(message,shift)
else:
    pass

    


        



