line="abp bwy ctyst\ndiooh\teno fkln\ngk1"
words = line.split()
tab=[]
for x in words:
    tab.append(len(x))

long = sum(tab)
print(long)