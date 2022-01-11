# Write a program to find the distinct pair of numbers whose product is even from a tuple of integers.
ele=input("Enter the elements of tuple: ").split()
tup=tuple(ele)
for i in range(len(tup)):
    for j in range(i+1,len(tup)):
        a=int(tup[i])
        b=int(tup[j])
        if (a*b)%2==0:
            t=(tup[i],tup[j])
            print(t)
