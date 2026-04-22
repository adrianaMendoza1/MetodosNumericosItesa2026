def f(x):
    return x**3 - x - 1

def regla_falsa(a, b, tol):
    if f(a) * f(b) >= 0: return None
    for i in range(100):
        c = b - (f(b) * (b - a)) / (f(b) - f(a))
        if abs(f(c)) < tol: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return c

print(f"Raíz Ejercicio 5: {regla_falsa(1, 2, 0.0001)}")