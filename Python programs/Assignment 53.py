# Write a program to print random numbers infinitely. Raise the StopIteration exception after displaying 10 numbers to exit from the program.

def display(n):
    while True:
        try:
            n+=1
            if n==11:
                raise StopIteration
        except StopIteration:
            break
        else:
            print(n,end=" ")
i=0
display(i)
                
                
