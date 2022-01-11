p,c = 0,0
while(True):
 num=int(input("Enter a number:"))
 if num==-1:
    break
 else:
    if num > 1:
     for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            c=c+1
            break
     else:
        p=p+1
        
        
print("Number of Prime numbers=",p,";Number of Composite numbers=",c)  
