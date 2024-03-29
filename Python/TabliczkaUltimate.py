import random
import re

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

def isIntegerStr(x):
    try:
        x = int(x)
        return True
    except ValueError:
        return False

def promptInt(question):
    res = ''
    while True:
        print(question, end='')
        res = input()
        if isIntegerStr(res):
            res = int(res)
            break
    return res

def promptPosInt(question):
    res = ''
    while True:
        print(question, end='')
        res = input()
        if isIntegerStr(res) & (int(res) > 0):
            res = int(res)
            break
    return res

def promptRegExp(question, regexp):
    res = ''
    while True:
        print(question, end='')
        res = input()
        if re.compile(regexp).match(res):
            break
    return res

def test(minlimit, maxlimit, posresults, exercises, operations):
    result = 0
    for i in range(exercises):
        a = random.randint(minlimit, maxlimit)
        b = random.randint(minlimit, maxlimit)
        los = random.choice(operations)
        match los:
            case '+':
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
            case '-':
                while (posresults) and (b > a):
                    b = random.randint(minlimit, maxlimit)
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
            case '*':
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
            case '/':
                while (b == 0):
                    b = random.randint(minlimit, maxlimit)
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
            case other:
                pass
    return result

# ------------------------------------------------------------------------------------
# ustalenie warunków testu
exercises  = promptPosInt("Podaj liczbę ćwiczeń:              ")
maxlimit   = promptPosInt("Podaj maksymalny czynnik:          ")
minlimit   = promptRegExp("Czy mają być liczby ujemne? [ynN]: ", r'^[ynN]$')
operations = promptRegExp("Podaj listę instrukcji [+-*/]:     ", r'^[\+\-\*\/]+$')

match minlimit:
    case 'y':
        minlimit = -maxlimit
        posresults = False
    case 'n':
        minlimit = 0
        posresults = False
    case 'N':
        minlimit = 0
        posresults = True
    case other:
        pass
print()

# mechanizm testowy
result = test(minlimit, maxlimit, posresults, exercises, operations)

print()

# napisz wynik
print(f"Wynik: {result}/{exercises} = {result/exercises*100}%")
if (result == exercises):
    print("Bezbłędnie! Brawo! :D")
