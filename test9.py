x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

z = x.intersection(y)
print("intersection of sets",z)

z = x.union(y)
print("Union of sets",z)

z = x.difference(y)
print("difference of sets",z)

z = x.symmetric_difference(y)
print("symetric of sets",z)

x.clear()
