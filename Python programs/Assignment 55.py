# Write a program to read the age of a person and raise exceptions if age is negative.

try:    
    age = int(input("Enter the age:"))    
    if(age<0):    
        raise ValueError   
    else:    
        print("the age is valid")    
except ValueError:    
    print("The age is not valid") 
else:
    print("No exception")
