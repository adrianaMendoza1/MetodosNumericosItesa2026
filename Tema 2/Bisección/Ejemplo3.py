import math

def f(x):
    return math.cos(x) - x

def biseccion(a, b, tol):
    if f(a) * f(b) >= 0:
        return "El método falla en este intervalo."
    while (b - a) / 2.0 > tol:
        c = (a + b) / 2.0
        if f(c) == 0: break
        if f(a) * f(c) < 0: b = c
        else: a = c
    return c

print(f"Raíz Ejercicio 3: {biseccion(0, 1, 0.0001)}")