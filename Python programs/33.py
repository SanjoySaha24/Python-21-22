# Write a program to accept a sequence of comma-separated numbers from the user and generate a tuple with those numbers.
elements=input("Enter a sequence of comma-separated numbers: ").split(",")
tuple=tuple(elements)
print("Tuple: ",tuple)
