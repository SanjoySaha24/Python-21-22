num= int(input("Til which number you want the sum:"))
n1, n2 = 0, 1
sum=0
while n1 < num:
    if (n1%2)==0:
        #print(n1):to print even terms
        sum=sum+n1
    nth = n1 + n2
    n1 = n2
    n2 = nth
print("Sum of the even terms of the fibonacci series upto",num,"is=",sum)
