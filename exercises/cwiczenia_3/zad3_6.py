x=5 #szerokość
x=x+1
y=5 #wysokość
L = []
for i in range(y):
    for j in range(x):
        L.append("+")
        if j != x -1:
            L.append("---")
    L.append("\n")
    for j in range(x):
        L.append("|   ")
    L.append("\n")

for j in range(x):
    L.append("+")
    if j != x -1:
        L.append("---")

result1 = "".join(L)
print(result1)