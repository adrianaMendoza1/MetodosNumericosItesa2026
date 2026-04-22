import math
def f(x):
    return math.cos(x) - x

def df(x):
    return -math.sin(x) - 1

def newton(x0, tol):
    for i in range(100):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol: return x1
        x0 = x1
    return x0

print(f"Raíz Ejercicio 3: {newton(1, 0.0001)}")