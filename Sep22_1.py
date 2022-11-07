
#creating function that convert decimal to binary
def decTohex(n):
    conversion_table = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A' , 'B', 'C', 'D', 'E', 'F']
    if(n<=0):
        return ''
    remainder = n%16
    return  decTohex(n//16)+conversion_table[remainder]
#printing the heading
print("Decimal   hexadecimal    binary")

#printing number from 0 to  15
for e in range(0,16):
    print(e,"     ",bin(e).replace("0b", ""),"     ",decTohex(e))