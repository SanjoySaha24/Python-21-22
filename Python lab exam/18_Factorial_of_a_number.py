# 18. Write a program for the factorial of a number. 

num = int(input("Enter a no. : "))
fact = 1
if num < 0:
    print("no factorial.")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1, num + 1):
        fact =fact * i
    print("factorial of",num,"is",fact)