A = [1, 2, 3, 4]
B = [3, 4, 5, 6]

A = "smok"
B = "sarna"
a_result = list(set(A) & set(B))
print("Podpunkt A:", a_result)

b_result = list(set(A) | set(B))
print("Podpunkt B:", b_result)