def unique(list):
    uniqueList = []
    for i in list:
        if i not in uniqueList:
            uniqueList.append(i)
    return uniqueList


list = input("Enter a elements to insert in list: ").split()

print('Unique elements in the list are : ', unique(list))