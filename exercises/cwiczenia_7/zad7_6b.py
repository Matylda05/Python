import random

it = (random.choice(["N", "E", "S", "W"]) for _ in iter(int, 1))

for _ in range(10):
    print(next(it))  