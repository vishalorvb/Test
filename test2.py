
#this function will return  miles earned on ticket_cost...
def getmiles(miles,ticket_cost):
    ticket_cost = int(ticket_cost)
    if miles < 25000:
        return ticket_cost *5
    if miles >=25000 and miles < 50000:
        return ticket_cost*7
    if miles >= 50000 and miles <75000:
        return ticket_cost*8
    if miles >= 75000 and miles <125000:
        return ticket_cost*9
    if miles >= 125000 :
        return ticket_cost*11
    
#This function take miles as input and return current plan as string    
def getplan(miles):
    if miles < 25000:
        return "Base"
    if miles >=25000 and miles < 50000:
        return "Silver"
    if miles >= 50000 and miles <75000:
        return "Gold"
    if miles >= 75000 and miles <125000:
        return"Platinum"
    if miles >= 125000 :
        return "Daimond"
    
        

#Taking user input
name = input("What is the customer's name ?\n") 
member = input("Is the customer a member(y/n)?\n")  
miles = int(input("How many miles does the customer have?\n"))
ticket_cost = int(input("What was the cost of their ticket?\n"))
#cheking for invalid input
#if user input is invalid than program will terminate
if (member != 'y' or member !='n') and miles < 0 and ticket_cost < 0:
    print("Error:  Number of miles or ticket cost is less than zero.")
    quit()


#printing output
print("Dear ",name)
print("              ")

#printing when customer is a member
if member == 'y':
    print("You are a member of SpartanAir loyalty rewards and are currently at Base tier.")
    print("Your recent ticket purchase of $",ticket_cost ,"has earned you ",getmiles(miles, ticket_cost) ,"miles")
    print("Your total number of miles has increased from", miles ,"miles to", miles+getmiles(miles, ticket_cost) ,"miles.")
    print("You are eligible for a status upgrade from", getplan(miles)," to ",getplan( miles+getmiles(miles, ticket_cost)),".")
#printing when customer in not a member
if member == 'n':
    print("SpartanAir would like to invite you to become a loyalty rewards member.")
    print("As a ",getplan(miles) ,"tier member, your recent ticket purchase of $",ticket_cost ,"would earn you", getmiles(miles, ticket_cost)," miles.")
         


    
