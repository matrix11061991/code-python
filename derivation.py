# : function that calculates derivate of functions
from sympy import symbols, cos, diff

a, b, c = symbols('a b c', real=True)
f = a**b - a**c + c**b

# differntiating function f in respect to a
print(diff(f, a))
