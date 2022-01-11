n=int(input("Enter the limit :: "))
c=0
for i in reversed(range(n)):
    if(i%2!=0):
        print(" "* c , "*" * i)
        c+=1

    