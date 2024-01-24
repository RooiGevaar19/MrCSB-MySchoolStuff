import math

a = float(input("podaj długość pierwszej przeciwprostokątnej "))
b = float(input("podaj długość drugiej przeciwprostokątnej "))
c = math.sqrt(a*a + b*b) 
print(f"przeciwprostokatna: {c}")