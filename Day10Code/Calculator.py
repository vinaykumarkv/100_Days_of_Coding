def add(n1,n2):
    return n1+n2

def sub(n1,n2):
    return n1-n2

def mul(n1,n2):
    return n1*n2

def div(n1,n2):
    return n1/n2




def calculator():
    operations = {"+": add, "-": sub, "*": mul, "/": div}
    num1 = int(input("please provide 1st number: "))
    m = "y"
    while m != "n":
        
        for i in operations:
            print (f"{i}:{operations[i]}")
        sym=input("Please pick an operation to perform : ")
        num2 = int(input("please provide the number to continue calculation : "))
        function = operations[sym]
        answer = function(num1,num2)
        print(f"{num1} {sym} {num2} = {answer}")
        m=input("Please pick 'y' to continue operation previous result or to stop provide 'n': ")
        if m =="n":
            break
        
calculator()