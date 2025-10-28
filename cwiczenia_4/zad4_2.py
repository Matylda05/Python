def make_ruler(x): 
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
    r = []
    r.append(result1)
    r.append("\n")
    r.append(result2)
    result = "".join(r)
    return result


def make_grid(x, y):
    x=x+1
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
    return result1

rows=5 
cols=7 
n = 35
print(make_ruler(n))
print(make_grid(rows, cols))