n=int(input("Enter the limit :: "))
c=0
for i in range(1,n+1):
    for j in range(i):
        c+=1
        print(c," ",end="")
    print()