# Write a program to display unique and duplicate elements of a tuple.
ele=input("Enter the elements of tuple: ").split()
tup=tuple(ele)
uni=[]
dup=[]
for i in tup:
    if i in uni:
        dup.append(i)
        uni.remove(i)
    else:
        uni.append(i)
uni=tuple(uni)
dup=tuple(dup)
print("Unique elements are: ",uni)
print("Duplicate elements are: ",dup)
