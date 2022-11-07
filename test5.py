#Defining the function

def GetVolume(r,R,H):

    # Calculating value of d

    d = 3*R - H

    Conical_Volume = 0

    Cylindrical_Volume = 0

    #Checking id value of d < R

    #Calculating value of conical part when d < R

    if d < R:

     Conical_Volume = (3.14* (r*r) * d)//3

    # Calculating value of Conical part if d==R

    if d == R :

        Conical_Volume = (3.14* (r*r) * R) // 3

    # Calculating total value in case d>R

    if d > R:

        Conical_Volume = (3.14* (r*r) * R) // 3

        Cylindrical_Volume = 3.14* (r*r) * (d-R)

    #Returning Sum of volume

    return Conical_Volume + Cylindrical_Volume



# Calling function and printing volume

print(GetVolume(11.2, 5, 5))

print(GetVolume(4, 5, 5))