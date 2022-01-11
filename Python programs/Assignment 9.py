a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

if a > b:
    a,b = b,a
elif a > c:
    a,c = c,a
else:
    b,c = c,b
    
print (a, "<", b, "<", c)