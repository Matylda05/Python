L=[1, 22, 333, 4, 55, 666, 77, 888, 9]
for idx, x in enumerate(L):
    y = str(x)
    dl=len(y)
    if dl < 3:
        L[idx] = y.zfill(3)

print(L)