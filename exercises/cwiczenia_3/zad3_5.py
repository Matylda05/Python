x = 35
x=x+1
L = []
L2 =[]

for i in range(x):
    L.append("|")
    if i != x -1:
        L.append("...")


for i in range(x):
    L2.append(i)
    if i > 9:
        L2.append("  ")
    else:
        L2.append("   ")

result1 = "".join(L)
result2 = "".join( str(x) for x in L2)
print(result1)
print(result2)