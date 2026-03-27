line="abp bwy ctyst\nnajwiekszy\teno fkln\ngk1"
words = line.split()
tab=[]
for x in words:
    tab.append(len(x))

maxx = max(words, key=len)
print("wyraz:", maxx)
print("długość wyrazu: ", len(maxx))
