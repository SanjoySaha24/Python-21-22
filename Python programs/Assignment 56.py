#  Write a program to print each line of a file in reverse order.

def revline(x):
    i=0
    fileContents=len(open(x).readlines())
    line1=[None]*fileContents
    f=open(x)
    while(i<fileContents):
        line1[i]=f.readline()
        line1[i]=line1[i].strip()
        print(line1[i][::-1])
        i=i+1
filename=input("Enter the file name : ")
revline(filename)
