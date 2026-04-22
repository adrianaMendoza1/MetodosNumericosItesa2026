# Archivo: Ejercicio2.py
import math

def f(x):
    return math.sqrt(x)

def regla_simpson(a, b, n):
    h = (b - a) / n
    suma = f(a) + f(b)
    for i in range(1, n):
        xi = a + i * h
        suma += (4 * f(xi) if i % 2 != 0 else 2 * f(xi))
    return (h / 3) * suma

print(f"Ejercicio 2 - Integral de sqrt(x): {regla_simpson(1, 4, 100):.4f}")