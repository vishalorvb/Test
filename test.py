

def Isleapyear(year):
    # Python program to check if year is a leap year or not
    # To get year (integer input) from the user
    # year = int(input("Enter a year: "))

    # divided by 100 means century year (ending with 00)
    # century year divided by 400 is leap year
    if (year % 400 == 0) and (year % 100 == 0):
        return True

    # not divided by 100 means not a century year
    # year divided by 4 is a leap year
    elif (year % 4 ==0) and (year % 100 != 0):
        return True
    # if not divided by both 400 (century year) and 4 (not century year)
    # year is not leap year
    else:
        return False
    
def printleap(start,end):
    #checking if firstyear > lastyear
    #swaping value if firstyear > lastyear
    if start > end:
        start,end = end,start
    #looping through each year   
    for e in range(start,end+1):
        #checking if year is leap or not? and printing
        if Isleapyear(e):
            print(e)    
            
firstyear = int(input("Please enter the first year"))  
lastyear = int(input("Please enter the last year"))     

printleap(firstyear, lastyear)     
            