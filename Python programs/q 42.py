names = [ "Virat Kholi","M.S Dhoni","Srikar Bharat","Shreyas Iyer","Ishant Sharma"]
print("Enter the runs scored by each player respectively(seprated by comma)\n",names)
score = input()
score = score.split(",")
dict={}
i = 0
for name in names:
    item = int(score[i])
    dict[name] = item
    i = i +1
search = input("\nWhich player score are you searching for? ")
if search not in dict:
    print("-1")
else:
    print(dict[search])



