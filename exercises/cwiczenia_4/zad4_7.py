def flatten(sequence):
    result = []
    for i in sequence:
        if isinstance(i, (list, tuple)):
            result += flatten(i)
        else:
            result.append( i)
    return result





lista = [ 
    0,
    (1, 2, 3),         
    4,         
    [5, 6, [7,8,9,10]],        
    11,
    [],
    (12, [13, 14,15,16]),
    [17,(18,19,20)]     
]
print(flatten(lista))