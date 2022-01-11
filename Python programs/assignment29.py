list1 = []
num1 = int(input('Enter size of list 1: '))
for n in range(num1):
    num1 = int(input('Enter element: '))
    list1.append(num1)
 
list2 = []
num2 = int(input('Enter size of list 2: '))
for n in range(num2):
    num2 = int(input('Enter element: '))
    list2.append(num2)

union_list = []

for x in list1:
    union_list.append(x)

for y in list2:
    if y in list1:
        pass
    else:
        union_list.append(y)

print("The union of the two lists is", union_list)