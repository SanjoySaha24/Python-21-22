# Write a program to count the frequency of all the elements in a tuple.
def count(tup, x):
	count = 0
	for ele in tup:
		if (ele == x):
			count = count + 1
	return count

ele=input("Enter the elements of tuple: ").split()
tup=tuple(ele)
li=[]
for i in tup:
    if i not in li:
        li.append(i)
for i in li:
    print("Frequency of",i,"is: ",count(tup,i))
