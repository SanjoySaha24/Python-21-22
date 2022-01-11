import prime

num = int(input("Enter a number: "))
if prime.primeCheck(num) == True:
    print("\nThe Number is a Prime Number")
else:
    print("\nThe Number is not a Prime Number")