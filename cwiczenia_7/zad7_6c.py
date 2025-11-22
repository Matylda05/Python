import itertools

dni_tygodnia = itertools.cycle(range(0, 7))

for _ in range(15):
    print(next(dni_tygodnia))  