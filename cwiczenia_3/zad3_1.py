#Czy podany kod jest poprawny składniowo w Pythonie? Jeśli nie, to dlaczego?

'''
#a)
x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
print(result)
#kod jest poprawny składniowo
'''

'''
#b)
for i in "axby": if ord(i) < 100: print (i)
# kod nie jest poprawny, ponieważ w pythonie nie 
# można pisać instrukcji if bezpośrednio po dwukropku w 
# pętli, bez przejścia do nowej lini lub jak w podpukcie c
#z użyciem operatora warunkowego
'''
'''
#c)
for i in "axby": print (ord(i) if ord(i) < 100 else i)
#kod jest poprawny składniowo
'''