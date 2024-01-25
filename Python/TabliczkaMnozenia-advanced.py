import random

def test(limit, exercises):
    result = 0
    for i in range(exercises):
        a = random.randint(0, limit)
        b = random.randint(0, limit)
        print(f"{i+1}: \t{a} * {b} = ", end='')
        guess = int(input())
        if (guess == a*b):
            print('Dobrze!')
            result += 1
        else:
            print(f'Poprawny wynik to {a*b}')
    return result

# ustalenie warunków testu
print("Podaj liczbę ćwiczeń:     ", end='')
exercises = int(input())
print("Podaj maksymalny czynnik: ", end='')
limit = int(input())

print()

# mechanizm testowy
result = test(limit, exercises)

print()

# napisz wynik
print(f"Wynik: {result}/{exercises} = {result/exercises*100}%")
if (result == exercises):
    print("Bezbłędnie! Brawo! :D")