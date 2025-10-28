def odwracanie(L, left, right):
    while left < right:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
    return L

def odwracanie_rekurencyjne(L, left, right):
    if left >= right:
        return L
    else:
        L[left], L[right] = L[right], L[left]
        left += 1
        right -= 1
        return odwracanie_rekurencyjne(L, left, right)

Lista = [0,1,2,3,4,5,6,7,8,9]

print(odwracanie(Lista, 4, 9))
print(odwracanie_rekurencyjne(Lista, 4, 9))