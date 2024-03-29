import random

def printOperation(i, a, b, sign):
    #print(f"{i}: \t{a} "+sign+f" {b} = ", end='')
    if (a < 0):
        print(f"{i}: \t({a}) ", end='')
    else:
        print(f"{i}: \t{a} ", end='')
    print(sign, end='')
    if (b < 0):
        print(f" ({b}) = ", end='')
    else:
        print(f" {b} = ", end='')

def test(limit, exercises):
    result = 0
    for i in range(exercises):
        a = random.randint(-limit, limit)
        b = random.randint(-limit, limit)
        los = random.randint(0,3)
        if (los == 0):
            printOperation(i+1, a, b, '-')
            try:
                guess = int(input())
                if (guess == a-b):
                    print('Dobrze!')
                    result += 1
                else:
                    print(f"Poprawny wynik to {a-b}")
            except ValueError:
                print(f"To nie jest liczba.")
        elif (los == 1):
            printOperation(i+1, a, b, '*')
            try:
                guess = int(input())
                if (guess == a*b):
                    print('Dobrze!')
                    result += 1
                else:
                    print(f"Poprawny wynik to {a*b}")
            except ValueError:
                print(f"To nie jest liczba.")
        elif (los == 2):
            while (b == 0):
                b = random.randint(-limit, limit)
            printOperation(i+1, a*b, b, '/')
            try:
                guess = int(input())
                if (guess == a):
                    print('Dobrze!')
                    result += 1
                else:
                    print(f"Poprawny wynik to {a}")
            except ValueError:
                print(f"To nie jest liczba.")
        else:
            printOperation(i+1, a, b, '+')
            guess = int(input())
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
