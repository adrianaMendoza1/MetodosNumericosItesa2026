import math
def f(x):
    return x * math.exp(x) - 1

def regla_falsa(a, b, tol):
    if f(a) * f(b) >= 0: return None
    for i in range(100):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(c)) < tol: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return c

print(f"Raíz Ejercicio 2: {regla_falsa(0, 1, 0.0001)}")