#Taking user input for ID
ID = int(input("Please Enter your ID"))

#Taking user input for course code
Course_Code = input("Please Enter your course code")

#Defining function to validate range if ID
def validateID(ID):
    if ID >= 60000000 and ID <= 69999999:
        return True
    return False

#Defining  function to validate length of course code
def validatecode(Course_Code):
    sub = Course_Code[0:4]
    if len(Course_Code) == 8 and sub == "INFS":
        return True
    return False

#validating usre input
if validateID(ID) == False:
    print(ID," is not valid Entry for Student ID. It must be between 60000000 - 69999999")
    
if validatecode(Course_Code) == False:
    print(Course_Code," is not valid entry for course code. It must be 8 character long")
    
if validatecode(Course_Code)  and validateID(ID):
    print("Thank you for entry,",ID,". You are registred in",Course_Code)
    
            
    
