import math
def f(x):
    return math.cos(x) + 2*x - 1

def secante(x0, x1, tol):
    for i in range(100):
        if f(x1) - f(x0) == 0: break
        x_nueva = x1 - (f(x1) * (x1 - x0)) / (f(x1) - f(x0))
        if abs(x_nueva - x1) < tol: return x_nueva
        x0, x1 = x1, x_nueva
    return x1

print(f"Raíz Ejercicio 2: {secante(0, 1, 0.0001)}")