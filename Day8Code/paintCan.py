
import math

height = int(input ("Please provide height of wall: "))
width = int(input ("Please provide width of wall: "))
coveragePerCan = int(input ("Please provide coverage per can of wall: "))

def numcan(height,width,coveragePerCan):
    numOfCans = (height*width)/coveragePerCan
    numOfCans = math.ceil(numOfCans)
    print(f"The number of cans required for painting the wall is :{numOfCans}")
    return numOfCans

nc = numcan(height,width,coveragePerCan)



