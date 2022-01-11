# Write a program to copy the content of the text file to another file by converting all lowercase characters to uppercase.

# # To open the first file in read mode
f1 = open("first.txt", "r")
# To open the second file in write mode
f2 = open("second.txt", "w")
l = f1.readline()
while l:
    f2.write(l.upper())
    l = f1.readline()
f1.close()
f2.close()
