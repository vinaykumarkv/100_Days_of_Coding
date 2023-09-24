def isLeapYear(year):
    

    if year%4 ==0:
        if year%100==0:
            if year%400==0:
                return True
                 
            else:
                return False
                 
        else:
            return True
             
    else:
        return False
    
def daysInMonth(year,month):
    monthDays = [31,28,31,30,31,30,31,31,30,31,30,31]
    if isLeapYear(year) == True and month == 2:
       return 29
     
    else:
        days = monthDays[month-1]
        return days

year = int(input("Please provide year: "))
month = int(input("please provide month: "))

Days = daysInMonth(year,month)
print(f"Number of days in selected month is {Days}.")



