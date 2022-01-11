#  Write a program to copy one Python script into another in such a way that all comment lines are skipped and not copied in the destination file.

# To open the first file in read mode
f = open("input.txt", "r")
# To open the second file in write mode
f1 = open("output.txt", "w")
l = f.readline()
while l:
    li = l.strip()
    if not li.startswith("#"):
         print (l.rstrip())
    l = f.readline()
    f1.write(l)
     
f.close()
f1.close()

