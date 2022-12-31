import sympy
# Définition de la variable symbolique x
x = sympy.symbols('x')
# Définition de la fonction f(x) = x^2
f = x**2
# Dérivation de la fonction f(x)
f_prime = f.diff(x)
print(f_prime)  # Affiche 2*x
