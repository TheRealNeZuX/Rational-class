class Rational:
    def GCD(a, b):
        while a!=0 and b!=0:
            if a>b:
                a%=b
            else:
                b%=a
        return a+b
    def __init__(self, value="0/1"):
        num=int(value.split("/")[0])
        den=int(value.split("/")[1])
        if den==0:
            raise ZeroDivisionError
        else:
            copy=abs(num)
            if den<0:
                num*=-1
                den*=-1
            self.num=int(num/Rational.GCD(copy, den))
            self.den=int(den/Rational.GCD(copy, den))
    def __str__(self):
        if self.num%self.den!=0:
            return f"{self.num}/{self.den}"
        else:
            return f"{self.num}"
    def __iter__(self):
        return iter((self.num, self.den))
    def __add__(self, other):
        return Rational(f"{self.num*other.den+other.num*self.den}/{self.den*other.den}")
    def __sub__(self, other):
        return Rational(f"{self.num*other.den-other.num*self.den}/{self.den*other.den}")
    def __mul__(self, other):
        return Rational(f"{self.num*other.num}/{self.den*other.den}")
    def __floordiv__(self, other):
        return Rational(f"{self.num*other.den}/{self.den*self.num}")
    def __lt__(self, other):
        if self.num*other.den<other.num*self.den:
            return True
        else:
            return False
    def __gt__(self, other):
        if self.num*other.den>other.num*self.den:
            return True
        else:
            return False
    def __ne__(self, other):
        if self.num*other.den!=other.num*self.den:
            return True
        else:
            return False
    def __le__(self, other):
        if self.num*other.den<=other.num*self.den:
            return True
        else:
            return False
    def __ge__(self, other):
        if self.num*other.den>=other.num*self.den:
            return True
        else:
            return False
    def __eq__(self, other):
        if self.num*other.den==other.num*self.den:
            return True
        else:
            return False
