names = ["Reetika","Surbhi","Aman","Pogo","Rohan"]
salaries =[5000,8500,5000,4800,10000]
dict = {}
i = 0
for name in names:
    dict[name] = salaries[i]
    i = i+1
print(dict)