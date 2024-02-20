print("Podaj rozmiar piramidy: ", end='')
n = int(input())

licznik = 0
for i in range(n+1):
    for j in range(i):
        print("*", end='')
        licznik += 1
    print()

print(licznik)
print(n*(n+1)/2)
