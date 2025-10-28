def fibonacci(n):
    x1 = 0
    x2 = 1
    for _ in range(n):
        x3 = x1 + x2
        x1 = x2
        x2 = x3
    return x1

print(fibonacci(19)) #4181