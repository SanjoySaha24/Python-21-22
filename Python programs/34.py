# Write a program to add elements in a tuple without using built-in functions.
ele=input("Enter a sequence of elements: ").split()
tup=tuple(ele)
sum=0
for i in tup:
    sum=sum+int(i)
print("Sum: ",sum)
