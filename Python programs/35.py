# Write a program to calculate the mean of elements in a tuple of integers.
ele=input("Enter the elements of tuple: ").split()
tup=tuple(ele)
sum=0
for i in tup:
    sum=sum+int(i)
    result=sum/len(tup)
print("Mean of the numbers: ",result)
