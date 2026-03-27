#Co jest złego w kodzie:

#L = [3, 5, 4] ; L = L.sort()       
#L.sort()  sortuje liste ale nie zwraca nowej listy tylko None, więc L = L.sort() po tym przypisaniu lista L zaiera None
#poprawny kod  L = [3, 5, 4] ; L.sort() 

#x, y = 1, 2, 3                     
#po lewej są tylko 2 wartości a po prawej 3, dlatego zgłasza się błąd "too many values to unpack"


#X = 1, 2, 3 ; X[1] = 4            
# po stworzeniu tuple w pythonie nie można modyfikować jej elemętów


#X = [1, 2, 3] ; X[3] = 4           
# listy są numerowane od 0 do n więc ta lista posiada tylko elenęty 0,1,2, nie posiada elemętu 3. Dlatego zgłasza się błąd "list assignment index out of range"


#X = "abc" ; X.append("d")          
# stringi w pythonie nie obsługują metody append, dlatego wysakyje bład "'str' object has no attribute 'append'"


#L = list(map(pow, range(8)))     
#metoda pow do wykonania potrzebuje 2 argumętów