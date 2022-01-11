x = int(input("Enter the value of x"))  
y = int(input("Enter the value of y"))

print("Before swapping numbers: %d   %d\n" %(x,y))  
temp = x
x = y
y = temp
 
print("Value of x:", x)
print("Value of y:", y)