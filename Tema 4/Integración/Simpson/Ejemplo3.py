# Archivo: Ejercicio3.py
import math

def f(x):
    return math.cos(x)

def regla_simpson(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        suma += (4 * f(xi) if i % 2 != 0 else 2 * f(xi))
    return (h / 3) * suma

print(f"Ejercicio 3 - Integral de cos(x): {regla_simpson(0, math.pi/2, 10):.4f}")