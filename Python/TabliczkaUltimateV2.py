import random
import re
import time

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

def test(minlimit, maxlimit, posresults, answers, exercises, operations):
    result = 0
    for i in range(exercises):
        a = random.randint(minlimit, maxlimit)
        b = random.randint(minlimit, maxlimit)
        los = random.choice(operations)
        match los:
            case '+':
                num1 = a
                num2 = b
                num3 = a+b
            case '-':
                while (posresults) and (b > a):
                    b = random.randint(minlimit, maxlimit)
                num1 = a
                num2 = b
                num3 = a-b
            case '*':
                num1 = a
                num2 = b
                num3 = a*b
            case '/':
                while (b == 0):
                    b = random.randint(minlimit, maxlimit)
                num1 = a*b
                num2 = b
                num3 = a
            case other:
                pass

        try:
            printOperation(i+1, num1, num2, los)
            guess = int(input())
            if (guess == num3):
                if (answers):
                    print('Dobrze!')
                result += 1
            else:
                if (answers):
                    print(f"Poprawny wynik to {num3}.")
        except ValueError:
            if (answers):
                print(f"To nie jest liczba. Poprawny wynik to {num3}.")
    return result

# ------------------------------------------------------------------------------------
# ustalenie warunków testu
exercises  = promptPosInt("Podaj liczbę ćwiczeń:              ")
maxlimit   = promptPosInt("Podaj maksymalny czynnik:          ")
timed      = promptRegExp("Czy mierzyć czas? [yn]:            ", r'^[yn]$')
answers    = promptRegExp("Czy pokazywać odpowiedzi? [yn]:    ", r'^[yn]$')
minlimit   = promptRegExp("Czy mają być liczby ujemne? [ynN]: ", r'^[ynN]$')
operations = promptRegExp("Podaj listę instrukcji [+-*/]:     ", r'^[\+\-\*\/]+$')

if (answers == 'y'):
    answers = True
else:
    answers = False

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
if (timed == 'y'):
    tm = time.perf_counter()
result = test(minlimit, maxlimit, posresults, answers, exercises, operations)
if (timed == 'y'):
    tm = time.perf_counter() - tm

print()

# napisz wynik
print(f"Wynik: {result}/{exercises} = {result/exercises*100}%")
if (timed == 'y'):
    print(f"Czas:  {round(tm,3)} s")
if (result == exercises):
    print("Bezbłędnie! Brawo! :D")
