import random

n = 10 # liczba rzutów

suma = 0
for krok in range(1, n+1):                    # powtarzaj poniższe kroki dla zmiennej "krok" od 1 do n
    rzut = random.randint(1, 6)               # random.randint() - losuj liczbę całkowitą od 1 do 6
    print(str(krok) + '. rzut: ' + str(rzut)) # str() - zamień liczbę na napis
    suma = suma + rzut
    
print('Suma:    ' + str(suma))
print('Średnia: ' + str(suma/n))

