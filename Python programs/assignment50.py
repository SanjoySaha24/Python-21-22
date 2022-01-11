import random

def shuffle(randList):
    for i in range(len(randList)):
        j = random.randint(0, len(randList)-1)
        randList[i], randList[j] = randList[j], randList[i]
    return randList

start, end = map(int, input("Enter the start and end range: ").split())
rList = [random.randint(start, end) for i in range(6)]

print("\nInitial list: ", rList)
print("Shuffled list: ", shuffle(rList))