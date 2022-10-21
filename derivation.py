# : function that calculates derivate of functions
from sympy import symbols, cos, diff
def calcDeriv(a, b, c)
  a, b, c = symbols('a b c', real=True)
  f = a**b - a**c + c**b
  # differntiating function f in respect to a
  return diff(f, a)


