import itertools

cykl = itertools.cycle(range(0, 2))

for _ in range(10):
    print(next(cykl))  