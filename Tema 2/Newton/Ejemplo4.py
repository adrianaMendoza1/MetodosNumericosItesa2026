import math
def f(x):
    return x**2 - math.log(x) - 5

def df(x):
    return 2*x - 1/x

def newton(x0, tol):
    for i in range(100):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol: return x1
        x0 = x1
    return x0

print(f"Raíz Ejercicio 4: {newton(2, 0.0001)}")