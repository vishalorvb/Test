#Taking user inpur
name = input("Please Enter Your Name")
Dob = int(input("Pleae Enter your year of Birth"))

#validating name
if len(name)<=2:
    print("Please Enter your entire name")
    quit()
    
#validating range of year    
if Dob  < 1990 or Dob > 2021:
    print("This is not valid entry for year of birth")
    quit()
   
#printing result    
print(name,",You are",2021-Dob,"Year old")    
    