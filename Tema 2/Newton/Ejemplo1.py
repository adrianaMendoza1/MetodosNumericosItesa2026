def f(x):
    return x**3 - x - 1

def df(x):
    return 3*x**2 - 1

def newton(x0, tol):
    for i in range(100):
        x1 = x0 - f(x0) / df(x0)
        if abs(x1 - x0) < tol: return x1
        x0 = x1
    return x0

print(f"Raíz Ejercicio 1: {newton(1.5, 0.0001)}")