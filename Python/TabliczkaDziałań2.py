import random

def test(limit, exercises, precision):
    result = 0
    for i in range(exercises):
        a = random.randint(0, limit*precision)*1.0/precision
        b = random.randint(0, limit*precision)*1.0/precision
        los = random.randint(0,1)
        if (los == 0):
            print(f"{i+1}: \t{a} - {b} = ", end='')
            try:
                guess = float(input())
                if (guess == a-b):
                    print('Dobrze!')
                    result += 1
                else:
                    print(f"Poprawny wynik to {a-b}")
            except ValueError:
                print(f"To nie jest liczba.")
        else:
            print(f"{i+1}: \t{a} + {b} = ", end='')
            guess = float(input())
            try:
                if (guess == a+b):
                    print('Dobrze!')
                    result += 1
                else:
                    print(f"Poprawny wynik to {a+b}")
            except ValueError:
                print(f"To nie jest liczba.")
    return result

# ustalenie warunków testu
print("Podaj liczbę ćwiczeń:                        ", end='')
exercises = int(input())
print("Podaj maksymalny czynnik:                    ", end='')
limit = int(input())
print("Podaj maksymalną liczbę miejsc po przecinku: ", end='')
precision = int(input())

print()

# mechanizm testowy
result = test(limit, exercises, 10**precision)

print()

# napisz wynik
print(f"Wynik: {result}/{exercises} = {result/exercises*100}%")
if (result == exercises):
    print("Bezbłędnie! Brawo! :D")
