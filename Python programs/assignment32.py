list = []

len = int(input("Enter number of elements: "))
for i in range(1, len + 1):
    num = int(input("Enter element %d: " %i))
    list.append(num)

print("The distinct pairs whose product is odd are: ")
for i in range(len):
    for j in range(i, len):
        product = list[i] * list[j]
        if (product%2!=0):
                print (list[i],"X", list[j])