num = int(input("Enter the range: "))
sum=0
for i in range (2,num+1):
    for j in range(2, int(i/2)+1):
        if (i % j) == 0:
            break
    else:
        sum=sum+i;
print("Sum of the prime numbers between 2 and",num,"is=",sum)
