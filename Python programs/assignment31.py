list1 = []
list2 = []
list3 = []

len1 = int(input("Enter number of elements in list 1: "))

for i in range(1, len1+1):
    num = int(input("Enter element %d: " %(i)))
    list1.append(num)

len2 = int(input("Enter number of elements in list 2: "))

for i in range(1, len2+1):
    num = int(input("Enter element %d: " %(i)))
    list2.append(num)

for x in list2:
        if x in list1:
            pass
        else:
            list3.append(x)

print(list3)