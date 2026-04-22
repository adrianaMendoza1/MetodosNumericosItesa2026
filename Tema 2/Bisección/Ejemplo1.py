def f(x):
    return x**3 - 4*x - 9

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0: return None
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return c

print(f"Raíz Ejercicio 1: {biseccion(2, 3, 0.0001)}")