def minmax (x):
    minimum = maximum = x[0]
    for i in x[1:]:
        if i < minimum: 
            minimum = i 
        else: 
            if i > maximum: maximum = i
    return (minimum,maximum)
list = []
n = int(input("Enter number of elements : "))
for i in range(0, n):
	ele = int(input())
	list.append(ele)
print("Minimum and Maximum numbers are",minmax(list))
