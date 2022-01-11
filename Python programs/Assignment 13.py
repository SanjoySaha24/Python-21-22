a=int(input("Enter The 1st no. : "))
b=int(input("Enter the 2nd no. : "))
i=1
while(i <= a and i <= b):
    if (a %i == 0 and b % i == 0):
        gcd = i
        i = i+ 1
        print("GCD is - ",gcd)