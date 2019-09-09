print([0 for i in range(3)])
from oop import partyanimal
class cricketfan(partyanimal):
    points=36
    def six(self):
        self.x=self.x+6
        self.points=self.points+self.x
        print(self.name,'The score is ',self.x, self.points)
    def __str__(self):
        return'({},{})'.format(self.x,self.points)
    def __add__(self, other):
        x= self.x+other.x
        points=self.points+other.points
        return(x,points)
s=cricketfan('preet')
j=partyanimal('jeet')
h=cricketfan('me')
s.six()
j.party()
s.six()
j.party()
s.party()
print(s)   # Here with the use of built-in function __str__() , the print(s)=s.__str__()=str(s) but it will not work on the j because that is the object of other class
s.__str__()
print(str(s))
format(s)
print(s+h)   # here __add__ is used as an operator overloading Like add and str there are so many operators which are built-in functions

class polygon:
    def __init__(self,no_of_sides):
        self.n=no_of_sides
        self.sides=[0 for i in range(no_of_sides)]
    def inputslides(self):
        self.sides=[float(input('Enter side '+str(i+1)+':'))for i in range(self.n)]
    def dispsides(self):
        for i in range(self.n):
            print('side',i+1,'is',self.sides[i])

class triangle(polygon):
    def __init__(self):
        polygon.__init__(self,3)
    def findarea(self):
        a,b,c=self.sides
        s=(a+b+c)/2
        area=(s*(s-a)*(s-b)*(s-c))**0.5
        print('The area of triangle is ',area)

t=triangle()
t.inputslides()
t.dispsides()
t.findarea()
print(isinstance(t,polygon))
print(isinstance(t,triangle))
print(issubclass(triangle,polygon))
print(issubclass(polygon,triangle))
'''Operator	Expression	Internally
Addition	=p1 + p2	p1.__add__(p2)
Subtraction	=p1 - p2	p1.__sub__(p2)
Multiplication=	p1 * p2	p1.__mul__(p2)
Power	= p1 ** p2	p1.__pow__(p2)
Division=	p1 / p2	p1.__truediv__(p2)
Floor Division=	p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)=	p1 % p2	p1.__mod__(p2)
Bitwise Left Shift=	p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift=	p1 >> p2	p1.__rshift__(p2)
Bitwise AND	=p1 & p2	p1.__and__(p2)
Bitwise OR	=p1 | p2	p1.__or__(p2)
Bitwise XOR	=p1 ^ p2	p1.__xor__(p2)
Bitwise NOT	= ~p1	p1.__invert__()'''

'''Less than	p1 < p2	p1.__lt__(p2)
Less than or equal to	p1 <= p2	p1.__le__(p2)
Equal to  p1 == p2	p1.__eq__(p2)
Not equal to	p1 != p2	p1.__ne__(p2)
Greater than	p1 > p2	p1.__gt__(p2)
Greater than or equal to	p1 >= p2	p1.__ge__(p2)'''