list1 = []
list2 = []
len1 = int(input("Enter number of elements in first list: "))
for i in range(1, len1+1):
            num = int(input("Enter element %d: " %(i)))
            list1.append(num)
len2 = int(input("Enter number of elements in second list: "))
for i in range(1, len2+1):
            num = int(input("Enter element %d: " %(i)))
            list2.append(num)

numbers = [y for x in [list1, list2] for y in x]

print("The concatenated list is", numbers)