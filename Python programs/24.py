def countOccurrences(str, word):
     
    a = str.split(" ")

    count = 0
    for i in range(0, len(a)):

        if (word == a[i]):
           count = count + 1
            
    return count      

str =input("Enter the string: ")
word =input("Enter the word: ")
print(countOccurrences(str, word))