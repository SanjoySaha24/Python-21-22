# Write a program to read a number from the user and print its square. Generate KeyboardIntrrupt exception if Ctrl + C is pressed instead of a number.

try:
    n=int(input("Enter the number: "))
    side=n*n
    print("Square of %d is %d " %(n,side))
except KeyboardInterrupt as e:
    print("You press Ctrl+C")
    print("Enter a number next time")
