def sum_seq(sequence):
    total = 0
    for i in sequence:
        if isinstance(i, (list, tuple)):
            total += sum_seq(i)
        else:
            total += i
    return total

lista = [ #suma 20
    (1, 1, 1),         
    1,         
    [1, 1, [1,1,1,1]],        
    1,
    [],
    (1, [1, 1,1,1]),
    [1,(1,1,1)]     
]
print(sum_seq(lista))