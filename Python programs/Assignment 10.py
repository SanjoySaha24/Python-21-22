p=int(input("Enter the principal amount :: "))

t=int(input("Enter the total no. of years :: "))
if(p<200000):
    si = p*0.1*t
    amt=p+si
elif(p<1000000):
    si = p*0.12*t
    amt = p+si
else:
    si = p*0.15*t
    amt = p+si

print("Your Final Amount is :: ",amt)