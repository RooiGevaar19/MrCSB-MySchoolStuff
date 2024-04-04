import random
import re
import time

def gcd(x, y):
    while(y):
       x, y = y, x % y
    return abs(x)

class Rational:
    nm = 0
    dm = 0
    def __init__(self, num, dem=1):
        self.nm = num
        self.dm = dem
    # convert to float
    def float(self):
        return self.nm/self.dm*1.0
    def int(self):
        return int(self.nm/self.dm)
    # return a fraction string
    def fraction(self):
        return f"{self.nm}/{self.dm}"
    # callibrate chars
    def callibrate(self):
        if (self.dm < 0):
            self.nm *= -1
            self.dm *= -1
        return self
    # reduce if possible
    def reduce(self):
        x = gcd(self.nm, self.dm)
        self.nm //= x
        self.dm //= x
        return self
    # typecast
    def __float__(self):
        return self.nm/self.dm*1.0
    def __int__(self):
        return int(self.nm/self.dm)
    def __str__(self):
        if (self.nm % self.dm == 0):
            return f"{self.int()}" 
        else:
            return f"{self.nm}/{self.dm}"
    # logic operators
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            #self = self.callibrate().reduce()
            #other = other.callibrate().reduce()
            #return (self.nm == other.nm) & (self.dm == other.dm)
            return ((self - other).nm == 0)
        elif isinstance(other, int):
            return (other == self.float())
        elif isinstance(other, float):
            return (other == self.float())
        else:
            return False
    def __ne__(self, other):
        return not self.__eq__(other)
    def __gt__(self, other):
        return float(self) > float(other)
    def __lt__(self, other):
        return float(self) < float(other)
    def __ge__(self, other):
        return float(self) >= float(other)
    def __le__(self, other):
        return float(self) <= float(other)
    # arithmetics
    def __add__(self, other):
        return Rational(self.nm*other.dm + self.dm*other.nm, self.dm*other.dm).callibrate().reduce()
    def __sub__(self, other):
        return Rational(self.nm*other.dm - self.dm*other.nm, self.dm*other.dm).callibrate().reduce()
    def __mul__(self, other):
        return Rational(self.nm*other.nm, self.dm*other.dm).callibrate().reduce()
    def __truediv__(self, other):
        return Rational(self.nm*other.dm, self.dm*other.nm).callibrate().reduce()
    def __neg__(self):
        return self * Rational(-1)
    def __pos__(self):
        return self * Rational(1)
    # functions
    def __abs__(self):
        res = Rational(self.nm, self.dm).callibrate()
        if (res.nm < 0):
            res.nm *= -1
        return res

class Equation:
    # ax+b = cx+d
    a = 0
    b = 0
    c = 0
    d = 0
    Solutions = 2 # 0 - no solutions, 1 - one solution, 2 - inf solutions
    def __init__(self, a1, b1, a2, b2):
        self.a = a1
        self.b = b1
        self.c = a2
        self.d = b2
        if ((self.a == self.c) & (self.b != self.d)):
            self.Solutions = 0
        elif ((self.a == self.c) & (self.b == self.d)):
            self.Solutions = 2
        else:
            self.Solutions = 1
    def __str__(self):
        if (self.a == 0):
            res = f""
        elif (self.a == 1):
            res = f"x "
        elif (self.a == -1):
            res = f"- x "
        elif (self.a < 0):
            res = f"- {abs(self.a)} x "
        else:
            res = f"{self.a} x "

        if (self.b < 0):
            res += f"- {abs(self.b)} "
        else: 
            if (res == f""):
                res += f"{self.b} "
            elif (self.b == 0):
                res += f""
            else:
                res += f"+ {self.b} "
        
        if (self.c == 0):
            res += f"= "
        elif (self.c == 1):
            res += f"= x "
        elif (self.c == -1):
            res += f"= - x "
        elif (self.c < 0):
            res += f"= - {abs(self.c)} x "
        else:
            res += f"= {self.c} x "

        if ((self.c == 0) and (self.d >= 0)):
            res += f"{self.d}"
        elif ((self.c != 0) and (self.d == 0)):
            res += f""
        elif (self.d < 0):
            res += f"- {abs(self.d)}"
        else:
            res += f"+ {self.d}"
        return res
    def addX(self, input):
        self.a += input
        self.c += input
        return self
    def addC(self, input):
        self.b += input
        self.d += input
        return self
    def mul(self, input):
        self.a *= input
        self.b *= input
        self.c *= input
        self.d *= input
        return self
    def div(self, input):
        if (self.a != 0):
            self.a /= input
        if (self.b != 0):
            self.b /= input
        if (self.c != 0):
            self.c /= input
        if (self.d != 0):
            self.d /= input
        return self
    def switch(self):
        pom1, pom2 = self.a, self.b
        self.a, self.b = self.c, self.d
        self.c, self.d = pom1, pom2
        return self
    def autosolve(self):
        self = self.addC(-self.b)
        self = self.addX(-self.c)
        if (eq.a == 0):
            self = self.switch()
        if (Solutions == 1):
            self = self.div(self.a)

for i in range(1,5):
    a = Rational(random.randint(-2,12),random.randint(1,6))
    b = Rational(random.randint(-2,12),random.randint(1,6))
    c = Rational(random.randint(-2,12),random.randint(1,6))
    d = Rational(random.randint(-2,12),random.randint(1,6))
    eq = Equation(a,b,c,d)
    print(eq)
    eq = eq.addC(-eq.b)
    print(eq)
    eq = eq.addX(-eq.c)
    print(eq)
    if (eq.a == 0):
        eq = eq.switch()
    if (eq.Solutions == 1):
        eq = eq.div(eq.a)
        print(eq)
    elif (eq.Solutions == 0):
        print('Równanie sprzeczne.')
    else:
        print('Równanie tożsamościowe.')
    print()